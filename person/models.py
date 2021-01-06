from django.db import models


class Person(models.Model):
    #  用户ID
    uid = models.AutoField(primary_key=True, verbose_name='用户ID')
    #  注册时间
    create_time = models.DateField(auto_now_add=True, verbose_name='注册时间')
    #  昵称
    nickname = models.CharField(max_length=20, verbose_name='用户昵称')
    #  联系电话
    telephone = models.CharField(max_length=20, verbose_name='手机号', help_text='18位数字', default='')
    # 头像
    profile_photo = models.ImageField(upload_to='profile', blank=True, null=True, verbose_name='头像')
    #  姓名
    name = models.CharField(max_length=20, verbose_name='真实姓名')
    #  性别
    sex_choices = (
        (0, '男'),
        (1, '女'),
    )
    sex = models.IntegerField(choices=sex_choices, default=0, verbose_name='性别')
    #  生日
    birthday = models.DateField(verbose_name='生日', blank=True, null=True)
    #  身高
    height = models.FloatField(help_text='cm', default=170, verbose_name='身高')
    #  现居地
    location = models.CharField(max_length=255, verbose_name='现居地')
    #  家乡
    hometown = models.CharField(max_length=255, verbose_name='家乡')
    #  学历
    education_choices = (
        (0, ''),
        (1, '大专以下'),
        (2, '大专'),
        (3, '本科'),
        (4, '硕士及以上')
    )
    education = models.IntegerField(choices=education_choices, default=0, verbose_name='学历')
    #  院校
    college = models.CharField(max_length=255, verbose_name='毕业院校')
    #  职业
    job = models.CharField(max_length=50, verbose_name='职业')
    #  月收入
    income = models.IntegerField(verbose_name='月收入')
    #  房产状态
    estate_choices = (
        (0, ''),
        (1, '已购房'),
        (2, '和父母同居'),
        (3, '租房'),
        (4, '其他')
    )
    estate = models.IntegerField(choices=estate_choices, default=0, verbose_name='房产状况')
    # 婚姻状况
    marriage_choices = (
        (0, ''),
        (1, '未婚'),
        (2, '离异'),
        (3, '丧偶'),
    )
    marriage = models.IntegerField(choices=marriage_choices, default=0, verbose_name='婚姻状况')
    #  倾心指数
    heart = models.IntegerField(default=0, verbose_name='倾心指数')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户管理'

    def __str__(self):
        return self.nickname
