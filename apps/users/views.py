# encoding:utf-8
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
# from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.conf import settings
from django.http import HttpResponse, JsonResponse

from .models import User, Address
from orders.models import OrderInfo
from areas.models import Area
from django.views.generic import View
from .forms import RegisterForm, LoginForm, AddressForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from celery_task.tasks import send_mail_active
from utils.mixin import LoginRequiredMixin


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
            user = User.objects.create_user(username=username, password=password, email=email,
                                            mobile=mobile)  # 如果是位置参数注意顺序和数量
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
        '''判断是否记住了用户名'''
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            print(username)
            checked = 'checked'
        else:
            username = ''
            checked = ''

        return render(request, 'login.html', {'username': username, 'checked': checked})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)  # 登录校验
            if user.is_active == 0:
                return render(request, 'login.html', {'err': '请到邮箱激活账户'})
            elif user is not None and user.is_active:
                login(request, user)  # 登录并记住状态
                response = redirect(reverse('good:index'))  # HttpResponseRedirect
                remember = request.POST.get('remember')
                if remember == 'on':  # 如果checkbox 的属性为on就表示勾选
                    response.set_cookie('username', username, max_age=7 * 24 * 3600)
                else:
                    response.delete_cookie('username')
                return response


            else:
                return render(request, 'login.html', {'form': form, 'msg': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'form': form})


class LogoutView(View):
    '''登出'''

    def get(self, request):
        logout(request)  # 清楚用户的session信息
        return redirect(reverse('good:index'))


class UserInforView(LoginRequiredMixin, View):
    '''用户信息'''

    def get(self, request):
        user = request.user
        '''积分控制会员等级'''
        num = 0
        if user.integral >= 1000:
            user.identity = 4
        elif 1000>user.integral >= 500:
            num = 1000-user.integral
            user.identity = 3
        elif 500>user.integral >= 200:
            num = 500 - user.integral
            user.identity = 2
        else:
            num = 200 - user.integral
            user.identity = 1
        user.save()

        return render(request, 'member_user.html', {'user': user, 'num': num})


class UserOrderView(LoginRequiredMixin, View):
    '''订单'''

    def get(self, request):
        user = request.user
        orders = OrderInfo.objects.filter(user=user)
        content = {
            'orders': orders
        }
        return render(request, 'member_order.html',content)


class GetProv(View):
    def get(self, request):
        '''获取所有省级地区的信息'''
        # 1.获取所有省级地区的信息
        areas = Area.objects.filter(aParent__isnull=True)
        # 2.遍历areas并拼接出json数据：atitle id
        areas_list = []
        for area in areas:
            areas_list.append((area.id, area.atitle))

        # 3.返回数据
        return JsonResponse({'data': areas_list})


class GetCity(View):
    def get(self, request, pid):
        '''获取pid的下级地区的信息'''
        # 1.获取pid对应地区的下级地区
        areas = Area.objects.filter(aParent__id=pid)
        # 2.遍历areas并拼接出json数据：atitle id
        areas_list = []
        for area in areas:
            areas_list.append((area.id, area.atitle))

        # 3.返回数据
        return JsonResponse({'data': areas_list})


class UserAddressView(LoginRequiredMixin, View):
    '''地址'''

    def get(self, request):
        user = request.user
        address = Address.objects.filter(user=user).order_by('id')
        print(user)
        print(address)
        times = [choice[1] for choice in Address.TIME_CHOICES]  # 获取models里的TIME_CHOICES选项
        content = {
            'addresses': address,
            'times': times,

        }
        return render(request, 'member_address.html', content)

    def post(self, request):
        form = AddressForm(request.POST)
        user = request.user  # 获取当前用户
        if form.is_valid():
            prov = form.cleaned_data['prov']
            city = form.cleaned_data['city']
            dis = form.cleaned_data['dis']
            receiver = form.cleaned_data['receiver']
            email = form.cleaned_data['email']
            place = form.cleaned_data['place']
            zip_code = form.cleaned_data['zip_code']
            mobile = form.cleaned_data['mobile']
            tel = form.cleaned_data['tel']
            landmark = form.cleaned_data['landmark']
            best_send_time = form.cleaned_data['best_send_time']
            address = Address.objects.filter(user=user)  # 获取当前用户地址
            if address:
                # 如果存在,　不设置为默认地址
                is_default = False
            else:
                # 如果不存在,　设置为默认地址
                is_default = True
            # city_id: 110000
            # district_id: 110101
            # province_id: 110000
            Address.objects.create(user=user, province_id=prov, city_id=city, district_id=dis, receiver=receiver,
                                   email=email, place=place,
                                   zip_code=zip_code, mobile=mobile, tel=tel, landmark=landmark,
                                   best_send_time=best_send_time, is_default=is_default)
            return redirect(reverse('user:address'))
        else:
            '''添加地址失败时, 地址栏仍然显示已有地址'''
            address = Address.objects.filter(user=user).order_by('id')
            print(user)
            print(address)
            times = [choice[1] for choice in Address.TIME_CHOICES]  # 获取models里的TIME_CHOICES选项
            content = {
                'addresses': address,
                'times': times,
                'form': form
            }
            return render(request, 'member_address.html', content)


class UserCollectView(LoginRequiredMixin, View):
    '''收藏'''

    def get(self, request):
        return render(request, 'member_collect.html')


class UserMsgView(LoginRequiredMixin, View):
    '''留言'''

    def get(self, request):
        return render(request, 'member_msg.html')


class UserPacketView(LoginRequiredMixin, View):
    '''红包'''

    def get(self, request):
        return render(request, 'member_packet.html')


class UserSafeView(LoginRequiredMixin, View):
    '''账户安全'''

    def get(self, request):
        return render(request, 'member_safe.html')


class UserMoneyView(LoginRequiredMixin, View):
    '''资金管理'''

    def get(self, request):
        return render(request, 'member_money.html')
