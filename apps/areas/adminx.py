# -*- coding: utf-8 -*-
# @Time    : 18-12-12 上午12:23
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : adminx.py
# @Software: PyCharm

from .models import Province, City
import xadmin


class ProvinceAdmin(object):
    list_display = ['id', 'province']

class CityAdmin(object):
    list_display = ['id', 'city']


xadmin.site.register(Province, ProvinceAdmin)
xadmin.site.register(City, CityAdmin)
