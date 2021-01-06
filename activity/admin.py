import datetime

from django.contrib import admin, messages
from django.http import JsonResponse

from django.contrib import admin
from activity.models import Activity
from person.models import Person


class UpdateListFilter(admin.SimpleListFilter):
    #  更新时间
    title = u'最近更新'
    parameter_name = 'update_days'

    def lookups(self, request, model_admin):
        return(
          ('0', '当日'),
          ('1', '最近1周'),
          ('2', '最近30天'),
        )

    def queryset(self, request, queryset):
        #  当前日期格式
        cur_date = datetime.datetime.now().date()

        if self.value() == '0':
            day = cur_date - datetime.timedelta(days=0)
            return queryset.filter(a_time=day)
        if self.value() == '1':
            day = cur_date - datetime.timedelta(days=7)
            return queryset.filter(a_time=day)
        if self.value() == '2':
            day = cur_date - datetime.timedelta(days=30)
            return queryset.filter(a_time=day)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('aid', 'nickname', 'a_time')
    list_per_page = 20

    search_fields = ('uid__nickname',)
    list_filter = ('a_time', UpdateListFilter)

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

    def make_copy(self, request, queryset):
        a_ids = request.POST.getlist('_selected_action')
        for aid in a_ids:
            activities = Activity.objects.get(aid=aid)

            Activity.objects.create(
                uid=activities.uid,
                nickname=activities.nickname,
                a_time=activities.a_time,
                a_content=activities.a_content,
                img1=activities.img1,
                img2=activities.img2,
                img3=activities.img3,
                img4=activities.img4,
            )
        messages.add_message(request, messages.SUCCESS, '复制成功，复制了{}个动态。'.format(len(a_ids)))

    make_copy.short_description = '复制'
