# -*- coding: utf-8 -*-
# @Time    : 18-12-12 上午12:23
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : adminx.py
# @Software: PyCharm

import xadmin
from .models import OrderInfo, OrderGoods


class OrderInfoAdmin(object):
    list_display = ['order_id', 'user', 'total_count', 'total_amount', 'pay_method', 'status']


class OrderGoodsAdmin(object):
    list_display = ['id', 'order', 'sku', 'count', 'price', 'comment', 'score', 'is_commented']


xadmin.site.register(OrderInfo, OrderInfoAdmin)
xadmin.site.register(OrderGoods, OrderGoodsAdmin)
