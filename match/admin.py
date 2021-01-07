import datetime
from django.contrib import admin, messages
from match.models import Match
from django.http import JsonResponse


class MatchListFilter(admin.SimpleListFilter):
    title = u'最近配对'
    parameter_name = 'match_time'

    def lookups(self, request, model_admin):
        return (
            ('0', u'当日'),
            ('1', u'最近7天'),
            ('2', u'最近15天'),
            ('3', u'最近30天'),
            ('4', u'2020年'),
            ('5', u'2019年及以前'),
        )

    def queryset(self, request, queryset):
        #  当前日期格式
        cur_date = datetime.date.today()
        if self.value() == '0':
            day = cur_date - datetime.timedelta(days=0)
            return Match.objects.filter(match_time__gte=day)
        if self.value() == '1':
            day = cur_date - datetime.timedelta(days=7)
            return Match.objects.filter(match_time__gte=day)
        if self.value() == '2':
            day = cur_date - datetime.timedelta(days=15)
            return Match.objects.filter(match_time__gte=day)
        if self.value() == '3':
            day = cur_date - datetime.timedelta(days=30)
            return Match.objects.filter(match_time__gte=day)
        if self.value() == '4':
            return Match.objects.filter(match_time__year=2020)
        if self.value() == '5':
            return Match.objects.filter(match_time_year__lte=2019)


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_id', 'a_uid', 'b_uid', 'match_time', 'status')
    list_per_page = 20

    search_fields = ('a_uid__nickname', 'b_uid__nickname')
    list_filter = ('status', 'match_time', MatchListFilter)
    list_editable = ('status',)

    raw_id_fields = ('a_uid', 'b_uid')

    actions = ('layer_input', 'make_copy',)

    actions_on_top = True
    save_on_top = True

    def layer_input(self, request, queryset):
        post = request.POST
        if not post.get('_selected'):
            return JsonResponse(data={
                'status': 'error',
                'msg': '请先选中数据'
            })
        else:
            return JsonResponse(data={
                'status': 'success',
                'msg': '处理成功'
            })

    layer_input.short_description = '更新'
    layer_input.type = 'success'
    layer_input_icon = 'el-icon-s-promotion'

    layer_input.layer = {
        'title': '配对信息更新',
        'tips': '输入更新配对信息',
        'confirm_button': '确认',
        'cancel_button': '取消',
        'width': '40%',
        'labelWidth': '80px',
        'params': [{
            'type': 'number',
            'key': 'input',
            'label': 'A用户的ID',
        }, {
            'type': 'number',
            'key': 'input',
            'label': 'B用户的ID'
        }, {
            'type': 'date',
            'key': 'date',
            'label': '配对时间',
        }, {
            'type': 'select',
            'key': 'type',
            'label': '恋爱状态',
            'value': '0',
            'options': [{
                'key': '0', 'label': '初识',
            }, {
                'key': '1', 'label': '牵手',
            }, {
                'key': '2', 'label': '失恋',
            }]
        }]
    }

    def make_copy(self, request, queryset):
        match_ids = request.POST.getlist('_selected_action')
        for match_id in match_ids:
            matches = Match.objects.get(match_id=match_id)

            Match.objects.create(
                a_uid=matches.a_uid,
                b_uid=matches.b_uid,
                match_time=matches.match_time,
                status=matches.status,
            )
        messages.add_message(request, messages.SUCCESS, '复制成功，复制了{}个配对记录。'.format(len(match_ids)))

    make_copy.short_description = '复制'
