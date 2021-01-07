import datetime
from django.db import models


class Article(models.Model):
    #  文章ID
    a_id = models.AutoField(primary_key=True, verbose_name='文章ID')
    #  用户ID
    uid = models.ForeignKey('person.Person', verbose_name='作者', on_delete=models.CASCADE)
    #  发表时间
    article_time = models.DateTimeField(verbose_name='发表时间', editable=True)
    #  更新时间
    #  update_time1 = models.DateTimeField(verbose_name='更新时间', editable=True, null=True, default=datetime.datetime.now())
    #  标题
    title = models.CharField(max_length=255, verbose_name='标题')
    #  文章内容
    article_content = models.TextField(verbose_name='文章内容', null=True, blank=True)
    #  文章配图(最多六张)
    article_img1 = models.ImageField(upload_to='art', blank=True, null=True)
    article_img2 = models.ImageField(upload_to='art', blank=True, null=True)
    article_img3 = models.ImageField(upload_to='art', blank=True, null=True)
    article_img4 = models.ImageField(upload_to='art', blank=True, null=True)
    article_img5 = models.ImageField(upload_to='art', blank=True, null=True)
    article_img6 = models.ImageField(upload_to='art', blank=True, null=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章管理'

    def __str__(self):
        return self.title
