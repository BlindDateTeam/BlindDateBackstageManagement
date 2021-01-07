import datetime
from django.db import models
from person.models import Person


class Activity(models.Model):
    aid = models.AutoField(primary_key=True, verbose_name='动态ID')  # 动态id
    #  用户id
    uid = models.ForeignKey('person.Person', verbose_name='用户ID', on_delete=models.CASCADE)
    #  用户昵称
    nickname = models.ForeignKey('person.Person', verbose_name='用户昵称', on_delete=models.CASCADE, related_name='ac_user', null=True)
    #  动态时间
    a_time = models.DateTimeField(verbose_name='动态时间', editable=True)
    #  更新时间
    #  update_time = models.DateTimeField(verbose_name='更新时间', editable=True, default=datetime.datetime.datetime(1, 1, 1, 1, 1, 1), null=True)
    #  文字内容
    a_content = models.TextField(verbose_name='文字内容', null=True, blank=True)
    #  最多四张配图
    img1 = models.ImageField(upload_to='act', blank=True, null=True)
    img2 = models.ImageField(upload_to='act', blank=True, null=True)
    img3 = models.ImageField(upload_to='act', blank=True, null=True)
    img4 = models.ImageField(upload_to='act', blank=True, null=True)

    class Meta:
        verbose_name = '动态'
        verbose_name_plural = '动态管理'

    def __str__(self):
        return str(self.uid) + '_' + str(self.a_time)
