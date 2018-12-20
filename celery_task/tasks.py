# -*- coding: utf-8 -*-
# @Time    : 18-12-20 下午3:43
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : task.py
# @Software: PyCharm

from django.core.mail import send_mail
from django.conf import settings
from celery import Celery

app = Celery('celery_task.tasks', broker='redis://127.0.0.1:6379/2')


@app.task()
def send_mail_active(to_email, username, token):
    '''
    发送激活邮件
    send_mail(subject, message, from_email, recipient_list,
              fail_silently=False, auth_user=None, auth_password=None,
              connection=None, html_message=None):
    '''
    subject = 'vmall商城'
    message = ''
    sender = settings.EMAIL_FROM
    receiver = [to_email]
    html_message = '<h1>%s, 欢迎您成为天天生鲜注册会员</h1>请点击下面链接激活您的账户<br/><a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>' % (
        username, token, token)

    send_mail(subject, message, sender, receiver, html_message=html_message)
