import datetime
from django.db import models


class Match(models.Model):
    #  匹配ID号
    match_id = models.AutoField(primary_key=True, verbose_name='匹配ID')
    #  对象A的ID
    a_uid = models.ForeignKey('person.Person', on_delete=models.CASCADE, related_name='a_user', verbose_name='对象A的昵称')
    #  对象B的ID
    b_uid = models.ForeignKey('person.Person', on_delete=models.CASCADE, related_name='b_user', verbose_name='对象B的昵称')
    #  匹配时间
    match_time = models.DateField(auto_now_add=True, verbose_name='匹配时间')
    #  更新时间
    #  update_time2 = models.DateField(verbose_name='变化时间', editable=True, default=datetime.date.today())
    #  恋爱状态
    status_choices = (
        (0, '初识'),
        (1, '牵手'),
        (2, '失恋'),
    )
    status = models.IntegerField(choices=status_choices, default=0, verbose_name='恋爱状态')

    class Meta:
        verbose_name = '匹配'
        verbose_name_plural = '匹配管理'

    def __str__(self):
        return str(self.a_uid) + ' match ' + str(self.b_uid)
