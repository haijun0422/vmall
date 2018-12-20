# -*- coding: utf-8 -*-
# @Time    : 18-12-12 上午12:23
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : adminx.py
# @Software: PyCharm

import xadmin
from .models import GoodsCategory1, GoodsCategory2, GoodsCategory3, GoodsChannel, Brand, Goods, GoodsSpecification, SpecificationOption, SKU, SKUImage, \
    SKUSpecification


class SKUAdmin(object):
    list_display = ['id', 'name', 'goods', 'category', 'price', 'market_price', 'stock', 'sales', 'comments',
                    'is_launched']


class GoodsCategoryAdmin1(object):
    list_display = ['id', 'name']


class GoodsCategoryAdmin2(object):
    list_display = ['id', 'name']


class GoodsCategoryAdmin3(object):
    list_display = ['id', 'name']


class GoodsChannelAdmin(object):
    list_display = ['group_id', 'category', 'index']


class BrandAdmin(object):
    list_display = ['id', 'name', 'first_letter']


class GoodsAdmin(object):
    list_display = ['id', 'name', 'brand', 'category1', 'category2', 'category3', 'sales', 'comments']


class GoodsSpecificationAdmin(object):
    list_display = ['id', 'goods', 'name']


class SpecificationOptionAdmin(object):
    list_display = ['id', 'spec', 'value']


class SKUImageAdmin(object):
    list_display = ['id', 'sku', 'image']


class SKUSpecificationAdmin(object):
    list_display = ['id', 'sku', 'spec', 'option']


xadmin.site.register(GoodsCategory1, GoodsCategoryAdmin1)
xadmin.site.register(GoodsCategory2, GoodsCategoryAdmin2)
xadmin.site.register(GoodsCategory3, GoodsCategoryAdmin3)
xadmin.site.register(GoodsChannel, GoodsChannelAdmin)
xadmin.site.register(Brand, BrandAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsSpecification, GoodsSpecificationAdmin)
xadmin.site.register(SpecificationOption, SpecificationOptionAdmin)
xadmin.site.register(SKU, SKUAdmin)
xadmin.site.register(SKUImage, SKUImageAdmin)
xadmin.site.register(SKUSpecification, SKUSpecificationAdmin)
