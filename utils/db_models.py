# -*- coding: utf-8 -*-
# @Time    : 18-12-12 上午12:11
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : db_models.py
# @Software: PyCharm

from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        # 抽象模型类，迁移文件此模型类不生成ＢａｓｅModel表
        abstract = True
