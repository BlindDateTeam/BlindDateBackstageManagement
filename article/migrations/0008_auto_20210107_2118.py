# Generated by Django 3.1.4 on 2021-01-07 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20210107_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_time',
            field=models.DateTimeField(verbose_name='发表时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_time1',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 7, 21, 18, 5, 302355), null=True, verbose_name='更新时间'),
        ),
    ]
