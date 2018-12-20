# -*- coding: utf-8 -*-
# @Time    : 18-12-13 下午1:21
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : adminx.py
# @Software: PyCharm

import xadmin
from xadmin import views
from .models import Address


class AddressAdmin(object):
    list_display = ['id', 'user']


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "电商后台"
    site_footer = "mall"
    menu_style = "accordion"


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

xadmin.site.register(Address, AddressAdmin)