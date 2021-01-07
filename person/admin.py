import datetime

from django.contrib import admin, messages
from django.http import JsonResponse

from person.models import Person

from simpleui.admin import AjaxAdmin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin


class BirthdayListFilter(admin.SimpleListFilter):
    title = u'最近生日'
    parameter_name = 'ages'

    def lookups(self, request, model_admin):
        return (
            ('0', u'最近7天'),
            ('1', u'最近15天'),
            ('2', u'最近30天'),
        )

    def queryset(self, request, queryset):
        # 当前日期格式
        cur_date = datetime.datetime.now().date()
        if self.value() == '0':
            # 前一天日期
            day = cur_date - datetime.timedelta(days=7)
            return queryset.filter(birthday__gte=day)
        if self.value() == '1':
            day = cur_date - datetime.timedelta(days=15)
            return queryset.filter(birthday__gte=day)
        if self.value() == '2':
            day = cur_date - datetime.timedelta(days=30)
            return queryset.filter(birthday__gte=day)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('uid', 'nickname', 'name', 'sex', 'birthday', 'create_time', 'telephone')
    search_fields = ('nickname', 'name')

    list_per_page = 20
    list_filter = ('sex', 'create_time', BirthdayListFilter)
    list_editable = ('sex', 'birthday', 'telephone')

    date_hierarchy = 'create_time'

    actions = ('layer_input', 'make_copy')

    actions_on_top = True
    save_on_top = True

    def layer_input(self, request, queryset):
        #  queryset进行数据过滤,只包含选中的数据
        post = request.POST
        #  获取到数据可进行业务处理
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

    #  指定为弹出层
    layer_input.layer = {
        'title': '用户数据更新',
        'tips': '输入用户更新信息',
        'confirm_button': '确认',
        'cancel_button': '取消',
        'width': '40%',
        #  表单中label的宽度,对应element-ui的label-width，默认80px
        'labelWidth': '80px',
        'params': [{
            'type': 'input',
            'key': 'name',
            'label': '用户昵称',
            'width': '200px',
        }, {
            'type': 'input',
            'key': 'name',
            'label': '手机号',
            'width': '200px',
        }, {
            'type': 'input',
            'key': 'name',
            'label': '真实姓名',
            'width': '200px',
        }, {
            'type': 'select',
            'key': 'type',
            'label': '性别',
            'value': '0',
            'size': 'small',
            'options': [{
                'key': '0', 'label': '男'
            }, {
                'key': '1', 'label': '女'
            }]
        }, {
            'type': 'input',
            'key': 'name',
            'label': '现居地',
        }, {
            'type': 'input',
            'key': 'name',
            'label': '家乡',
        }, {
            'type': 'select',
            'key': 'type',
            'label': '学历',
            'value': '0',
            'size': 'small',
            'options': [{
                'key': '0', 'label': ' '
            }, {
                'key': '1', 'label': '大专以下'
            }, {
                'key': '2', 'label': '大专'
            }, {
                'key': '3', 'label': '本科'
            }, {
                'key': '4', 'label': '研究生及以上'
            }]
        }, {
            'type': 'input',
            'key': 'name',
            'label': '职业',
            'width': '300px',
        }, {
            'type': 'number',
            'key': 'money',
            'label': '月收入',
            'value': 6000,
        }, {
            'type': 'select',
            'key': 'type',
            'label': '房产状况',
            'value': '0',
            'options': [{
                'key': '0', 'label': ' ',
            }, {
                'key': '1', 'label': '已购房',
            }, {
                'key': '2', 'label': '与父母同居',
            }, {
                'key': '3', 'label': '租房',
            }, {
                'key': '4', 'label': '其他',
            }]
        }, {
            'type': 'number',
            'key': 'number',
            'label': '倾心指数',
            'value': 0,
        }]
    }


    def make_copy(self, request, queryset):
        u_ids = request.POST.getlist('_selected_action')
        for uid in u_ids:
            people = Person.objects.get(uid=uid)

            Person.objects.create(
                nickname=people.nickname,
                create_time=people.create_time,
                telephone=people.telephone,
                name=people.name,
                profile_photo=people.profile_photo,
                sex=people.sex,
                birthday=people.birthday,
                height=people.height,
                location=people.location,
                education=people.education,
                college=people.college,
                job=people.job,
                income=people.income,
                estate=people.estate,
                marriage=people.marriage,
                heart=people.heart,
            )

        messages.add_message(request, messages.SUCCESS, '复制成功，复制了{}个员工。'.format(len(u_ids)))

    make_copy.short_description = '复制用户'
