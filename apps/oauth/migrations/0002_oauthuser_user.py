# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-15 01:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oauthuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
