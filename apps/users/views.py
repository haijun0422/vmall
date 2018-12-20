# encoding:utf-8
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.conf import settings
from django.http import HttpResponse


from .models import User
from django.views.generic import View
from .forms import RegisterForm, LoginForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from celery_task.tasks import send_mail_active


class CustomBackend(ModelBackend):
    '''定义用户名，邮箱和手机号都可以登录，setting里需要配置'''
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class RegisterView(View):
    '''
    注册
    /user/register
    所有验证放入了form表单
    '''
    def get(self, request):
        return render(request, 'regist.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            user = User.objects.create_user(username=username, password=password, email=email, mobile=mobile) # 如果是位置参数注意顺序和数量
            user.is_active = 0
            user.save()

            '''
            发送激活邮件，包含激活链接: http: // 127.0.0.1: 8000/user/active/id
            激活链接中需要包含用户的身份信息, 并且要把身份信息进行加密
            加密用户的身份信息，生成激活token
            '''
            serializer = Serializer(settings.SECRET_KEY, 3600)
            info = {'confirm': user.id}
            token = serializer.dumps(info)  # bytes
            token = token.decode()
            # 发邮件
            send_mail_active.delay(email, username, token)
            return redirect(reverse('user:login'))
        else:
            error = form.errors
        return render(request, 'regist.html', {'form': form, 'error': error})
class ActiveEmail(View):
    '''用户激活'''
    def get(self, request, token):
        '''进行解密,获取进行激活的用户信息'''
        serializer = Serializer(settings.SECRET_KEY, 3600)
        try:
            '''获取等待激活用户的id'''
            info = serializer.loads(token)
            user_id = info['confirm']
            '''根据id获取用户信息'''
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()
            return redirect(reverse('user:login'))
        except SignatureExpired as e:
            return HttpResponse('激活链接已经过期')



class LoginView(View):
    '''
    登录
    /user/login
    所有输入验证放入了form表单
    '''
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password) # 验证用户名和密码
            if user is not None and user.is_active:
                login(request, user)  # 登录
                return redirect(reverse('good:index'))
            else:
                return render(request, 'login.html', {'form': form, 'msg': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'form': form})
