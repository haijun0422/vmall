# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-29 18:18
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('areas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mobile', models.CharField(max_length=11, unique=True, verbose_name='手机')),
                ('email_activate', models.BooleanField(default=False, verbose_name='邮箱验证状态')),
            ],
            options={
                'verbose_name_plural': '用户',
                'db_table': 'tb_users',
                'verbose_name': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('receiver', models.CharField(max_length=20, verbose_name='收货人')),
                ('place', models.CharField(max_length=50, verbose_name='地址')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机')),
                ('zip_code', models.CharField(default=100000, max_length=10, verbose_name='邮编')),
                ('landmark', models.CharField(blank=True, max_length=20, null=True, verbose_name='标志建筑')),
                ('best_send_time', models.CharField(choices=[('am', '上午08点-12点'), ('pm', '下午12点-18点')], max_length=15, verbose_name='最佳配送时间')),
                ('tel', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='固定电话')),
                ('email', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='电子邮箱')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('city', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='city_addresses', to='areas.Area', verbose_name='市')),
                ('district', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='district_addresses', to='areas.Area', verbose_name='区')),
                ('province', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='province_addresses', to='areas.Area', verbose_name='省')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name_plural': '用户地址',
                'ordering': ['-update_time'],
                'db_table': 'tb_address',
                'verbose_name': '用户地址',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('type', models.SmallIntegerField(choices=[(1, '留言'), (2, '投诉'), (3, '询问'), (4, '售后')], verbose_name='留言类型')),
                ('title', models.CharField(max_length=50, verbose_name='主题')),
                ('content', models.TextField(max_length=200, verbose_name='留言内容')),
                ('file', models.FileField(blank=True, null=True, upload_to='user/file', verbose_name='上传文件')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name_plural': '用户留言',
                'db_table': 'tb_message',
                'verbose_name': '用户留言',
            },
        ),
        migrations.CreateModel(
            name='Packet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('rule', models.SmallIntegerField(choices=[(1, '满减'), (2, '折扣')], verbose_name='规则')),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='起始时间')),
                ('end_time', models.DateTimeField(auto_now_add=True, verbose_name='结束时间')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否启用')),
            ],
            options={
                'verbose_name_plural': '红包',
                'db_table': 'tb_packet',
                'verbose_name': '红包',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='default_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='users.Address', verbose_name='默认地址'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
