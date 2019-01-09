# -*- coding: utf-8 -*-
# @Time    : 18-12-18 下午3:23
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from .views import IndexView

urlpatterns = [
    url(r'', IndexView.as_view(), name='index'),
    # url(r'', CategoryListView.as_view(), name='category_list'),
    # url(r'^category/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name='category_detail'),
]
