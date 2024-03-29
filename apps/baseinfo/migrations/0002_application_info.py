# Generated by Django 2.1 on 2018-08-23 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_name', models.CharField(max_length=50, verbose_name='应用名称')),
                ('application_tag', models.CharField(max_length=50, unique=True, verbose_name='应用标识符')),
                ('application_owner', models.CharField(max_length=50, verbose_name='应用负责人')),
                ('application_department', models.CharField(max_length=50, verbose_name='应用部门')),
                ('application_desc', models.CharField(max_length=500, verbose_name='应用简介')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '应用类型',
                'verbose_name_plural': '应用类型',
            },
        ),
    ]
