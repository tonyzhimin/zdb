# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-31 15:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, verbose_name='实例名称')),
                ('role', models.SmallIntegerField(choices=[(1, 'master'), (2, 'slave'), (3, 'standby slave')], verbose_name='实例角色')),
                ('port', models.IntegerField(verbose_name='实例端口')),
                ('memory', models.IntegerField(verbose_name='实例内存')),
                ('admin_user', models.CharField(default='', max_length=30, verbose_name='管理用户')),
                ('admin_pass', models.CharField(default='', max_length=30, verbose_name='管理密码')),
                ('status', models.SmallIntegerField(verbose_name='实例状态')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '实例管理',
                'verbose_name_plural': '实例管理',
            },
        ),
        migrations.CreateModel(
            name='InstancesGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, verbose_name='实例组名称')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('business', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='cmdb.Business')),
            ],
            options={
                'verbose_name': '实例组管理',
                'verbose_name_plural': '实例组管理',
            },
        ),
        migrations.CreateModel(
            name='Mysqldbs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, verbose_name='库名')),
                ('status', models.SmallIntegerField(verbose_name='状态')),
                ('desc', models.TextField(verbose_name='业务用途')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databases.Instances')),
            ],
            options={
                'verbose_name': '业务库管理',
                'verbose_name_plural': '业务库管理',
            },
        ),
        migrations.CreateModel(
            name='Mysqlusers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, verbose_name='用户名')),
                ('passwd', models.CharField(max_length=30, verbose_name='密码')),
                ('from_ip', models.GenericIPAddressField(default='0.0.0.0', verbose_name='来源IP')),
                ('status', models.SmallIntegerField(verbose_name='用户状态')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('db', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databases.Mysqldbs')),
            ],
            options={
                'verbose_name': '用户管理',
                'verbose_name_plural': '用户管理',
            },
        ),
        migrations.CreateModel(
            name='Privileges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privi', models.SmallIntegerField(choices=[(1, '读写'), (2, '只读')], default=1, verbose_name='读写权限')),
                ('db', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databases.Mysqldbs')),
                ('instance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='databases.Instances')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databases.Mysqlusers')),
            ],
            options={
                'verbose_name': '权限管理',
                'verbose_name_plural': '权限管理',
            },
        ),
        migrations.AddField(
            model_name='instances',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databases.InstancesGroup'),
        ),
        migrations.AddField(
            model_name='instances',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Servers'),
        ),
    ]