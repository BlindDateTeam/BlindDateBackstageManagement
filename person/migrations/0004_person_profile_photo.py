# Generated by Django 3.1.4 on 2021-01-05 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_auto_20210105_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
