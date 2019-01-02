# -*- coding: utf-8 -*-
# @Time    : 18-12-12 上午12:23
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : adminx.py
# @Software: PyCharm

from .models import Area
import xadmin


class AreaAdmin(object):
    list_display = ['id', 'city_name']


xadmin.site.register(Area, AreaAdmin)

