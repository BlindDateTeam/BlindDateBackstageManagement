# Generated by Django 3.1.4 on 2021-01-07 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0007_auto_20210107_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='update_time',
            field=models.DateTimeField(null=True, verbose_name='更新时间'),
        ),
    ]
