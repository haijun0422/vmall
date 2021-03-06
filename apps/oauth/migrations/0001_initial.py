# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-09 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OAuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('openid', models.CharField(db_index=True, max_length=64)),
            ],
            options={
                'verbose_name': 'QQ用户',
                'verbose_name_plural': 'QQ用户',
                'db_table': 'tb_oauth',
            },
        ),
    ]
