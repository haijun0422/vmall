# -*- coding: utf-8 -*-
# @Time    : 18-12-7 下午5:24
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from users.views import RegisterView, LoginView


urlpatterns = [
    url(r'register', RegisterView.as_view(), name='register'),
    url(r'login', LoginView.as_view(), name='login'),

]