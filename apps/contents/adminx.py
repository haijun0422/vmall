# -*- coding: utf-8 -*-
# @Time    : 18-12-12 上午12:23
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : adminx.py
# @Software: PyCharm

import xadmin
from .models import ContentCategory, Content


class ContentCategoryAdmin(object):
    list_display = ['id', 'name']


class ContentAdmin(object):
    list_display = ['id', 'title', 'url', 'status', 'sequence']


xadmin.site.register(ContentCategory, ContentCategoryAdmin)
xadmin.site.register(Content, ContentAdmin)
