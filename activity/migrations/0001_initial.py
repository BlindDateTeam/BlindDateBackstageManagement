# Generated by Django 3.1.4 on 2021-01-04 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('a_time', models.DateTimeField(auto_now_add=True)),
                ('a_content', models.CharField(max_length=500)),
                ('img1', models.ImageField(blank=True, null=True, upload_to='cag')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='cag')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='cag')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='cag')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.person')),
            ],
        ),
    ]
