# Generated by Django 3.1.4 on 2021-01-07 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0010_auto_20210107_2101'),
        ('match', '0003_auto_20210105_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='a_uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_user', to='person.person', verbose_name='对象A的昵称'),
        ),
        migrations.AlterField(
            model_name='match',
            name='b_uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b_user', to='person.person', verbose_name='对象B的昵称'),
        ),
    ]
