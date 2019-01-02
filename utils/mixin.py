# -*- coding: utf-8 -*-
# @Time    : 18-12-27 下午12:33
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : mixin.py
# @Software: PyCharm

from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)