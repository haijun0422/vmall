# -*- coding: utf-8 -*-
# @Time    : 18-12-7 下午5:24
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from users import views
from users.views import RegisterView, LoginView, ActiveEmail, LogoutView, UserInforView, UserOrderView, UserAddressView, \
    UserCollectView, UserMsgView, UserPacketView, UserSafeView, UserMoneyView, GetCity, GetProv

urlpatterns = [
    url(r'^register', RegisterView.as_view(), name='register'),
    url(r'^login', LoginView.as_view(), name='login'),
    url(r'^active/(?P<token>.*)$', ActiveEmail.as_view(), name='active'),  # 邮箱激活
    url(r'^logout', LogoutView.as_view(), name='logout'),
    url(r'^member', UserInforView.as_view(), name='member'),
    url(r'^order', UserOrderView.as_view(), name='order'),
    url(r'^address', UserAddressView.as_view(), name='address'),
    url(r'^collect', UserCollectView.as_view(), name='collect'),
    url(r'^message', UserMsgView.as_view(), name='message'),
    url(r'^packet', UserPacketView.as_view(), name='packet'),
    url(r'^safe', UserSafeView.as_view(), name='safe'),
    url(r'^money', UserMoneyView.as_view(), name='money'),
    url(r'^prov', GetProv.as_view(), name='prov'),  # 获取所有省级地区的信息
    url(r'^city(\d+)$', GetCity.as_view(), name='city'),  # 获取省下面的市的信息
    url(r'^dis(\d+)$', GetCity.as_view(), name='dis'),  # 获取市下面的县的信息
    # url(r'^prov$', views.prov), # 获取所有省级地区的信息
    # url(r'^city(\d+)$', views.city), # 获取省下面的市的信息
    # url(r'^dis(\d+)$', views.city), # 获取市下面的县的信息

]
