# -*- coding: utf-8 -*-
# @Time    : 18-12-18 下午4:16
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : forms.py
# @Software: PyCharm

from django import forms
from .models import User
import re


def check_email(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)


def check_mobile(mobile):
    pattern = re.compile(r'^((13[0-9])|(14[5,7])|(15[0-3,5-9])|(17[0,3,5-8])|(18[0-9])|166|198|199|(147))\\d{8}$')
    return re.match(pattern, mobile)


class RegisterForm(forms.Form):
    # username = forms.CharField(label='用户名', widget=forms.TextInput(attrs={'class': 'l_user', 'placeholder': '请输入用户名'}))
    # password1 = forms.CharField(label='密码',
    #                             widget=forms.PasswordInput(attrs=({'class': 'l_pwd', 'placeholder': '请输入密码'})))
    # password2 = forms.CharField(label='确认密码',
    #                             widget=forms.PasswordInput(attrs=({'class': 'l_pwd', 'placeholder': '请再次输入密码'})))
    # email = forms.EmailField(label='邮箱', widget=forms.EmailInput(attrs=({'class': 'l_email', 'placeholder': '请输入邮箱'})))
    # mobile = forms.CharField(label='手机',
    #                          widget=forms.TextInput(attrs=({'class': 'l_tel', 'placeholder': '请输入手机号'})))

    username = forms.CharField(label='用户名', widget=forms.TextInput)
    password1 = forms.CharField(label='密码',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码',
                                widget=forms.PasswordInput)
    email = forms.EmailField(label='邮箱')
    mobile = forms.CharField(label='手机',
                             widget=forms.TextInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise forms.ValidationError('用户名至少5位')
        elif len(username) > 50:
            raise forms.ValidationError('用户名不能超过50位')
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError('用户名已存在')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if check_email(email):
            filter_result = User.objects.filter(email__exact=email)
            if len(filter_result) > 0:
                raise forms.ValidationError('邮箱已存在')
        else:
            raise forms.ValidationError('请输入正确邮箱')
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 6:
            raise forms.ValidationError('密码至少6位')
        elif len(password1) > 20:
            raise forms.ValidationError('密码不能超过20位')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('两次密码输入不一致')
        return password2

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if check_mobile(mobile):
            filter_result = User.objects.filter(mobile__exact=mobile)
            if len(filter_result) > 0:
                raise forms.ValidationError('手机号已存在')
            else:
                raise forms.ValidationError('请输入正确手机号')
        return mobile


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码', widget=forms.PasswordInput)
    '''判断登录方式'''
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if check_email(username):
            filter_result = User.objects.filter(email__exact=username)
            if not filter_result:
                raise forms.ValidationError('邮箱不存在')
        elif check_mobile(username):
            filter_result = User.objects.filter(mobile__exact=username)
            if not filter_result:
                raise forms.ValidationError('手机号不存在')
        else:
            filter_result = User.objects.filter(username__exact=username)
            if not filter_result:
                raise forms.ValidationError('用户名不存在')
        return username
