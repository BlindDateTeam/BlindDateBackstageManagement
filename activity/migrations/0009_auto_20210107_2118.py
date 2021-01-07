# Generated by Django 3.1.4 on 2021-01-07 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0008_auto_20210107_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='a_time',
            field=models.DateTimeField(verbose_name='动态时间'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 7, 21, 18, 5, 294376), null=True, verbose_name='更新时间'),
        ),
    ]