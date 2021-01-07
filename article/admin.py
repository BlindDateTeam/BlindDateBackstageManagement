import datetime
from django.contrib import admin, messages
from django.http import JsonResponse

from article.models import Article


class UpdateListFilter(admin.SimpleListFilter):
    #  根据更新时间来推荐
    title = u'最近更新'
    parameter_name = 'update_days'

    def lookups(self, request, model_admin):
        return (
            ('0', '当日'),
            ('1', '最近1周'),
            ('2', '最近30天'),
            ('3', '2020年'),
            ('4', '2019年及以前'),
        )

    def queryset(self, request, queryset):
        #  当前日期格式
        cur_date = datetime.datetime.now().date()
        if self.value() == '0':
            #  日期选定
            day = cur_date - datetime.timedelta(days=0)
            return Article.objects.filter(article_time__gte=day)
        if self.value() == '1':
            day = cur_date - datetime.timedelta(days=7)
            return Article.objects.filter(article_time__gte=day)
        if self.value() == '2':
            day = cur_date - datetime.timedelta(days=30)
            return Article.objects.filter(article_time__gte=day)
        if self.value() == '3':
            return Article.objects.filter(article_time__year=2020)
        if self.value() == '4':
            return Article.objects.filter(article_time__year__lte=2019)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('a_id', 'title', 'uid', 'article_time')
    list_per_page = 20

    actions = ('layer_input', 'make_copy',)
    search_fields = ('title', 'uid__nickname', 'article_time')
    list_filter = ('article_time', UpdateListFilter)
    list_editable = ('article_time',)

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
        'title': '文章信息更新',
        'tips': '更新文章信息',
        'confirm_button': '确认',
        'cancel_button': '取消',
        'width': '40%',
        'labelWidth': '80px',
        'params': [{
            'type': 'datetime',
            'key': 'datetime',
            'label': '更新时间',
        }, {
            'type': 'name',
            'key': 'input',
            'label': '文章标题',
            'width': '300px',
        }, {
            'type': 'text',
            'key': 'input',
            'label': '文章内容',
        }, {
            'type': 'img',
            'key': 'upload',
            'label': '文章附图1',
        }, {
            'type': 'img',
            'key': 'upload',
            'label': '文章附图2',
        }, {
            'type': 'img',
            'key': 'upload',
            'label': '文章附图3',
        }, {
            'type': 'img',
            'key': 'upload',
            'label': '文章附图4',
        }, {
            'type': 'img',
            'key': 'upload',
            'label': '文章附图5',
        }, {
            'type': 'img',
            'key': 'upload',
            'label': '文章附图6',
        }]
    }

    def make_copy(self, request, queryset):
        article_ids = request.POST.getlist('_selected_action')
        for article_id in article_ids:
            articles = Article.objects.get(a_id=article_id)

            Article.objects.create(
                uid=articles.uid,
                article_time=articles.article_time,
                title=articles.title,
                article_content=articles.article_content,
                article_img1=articles.article_img1,
                article_img2=articles.article_img2,
                article_img3=articles.article_img3,
                article_img4=articles.article_img4,
                article_img5=articles.article_img5,
                article_img6=articles.article_img6
            )

        messages.add_message(request, messages.SUCCESS, '复制成功，复制了{}篇文章。'.format(len(article_ids)))

    make_copy.short_description = '复制'
