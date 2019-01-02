# encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.db_models import BaseModel


class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机')
    email_activate = models.BooleanField(default=False, verbose_name='邮箱验证状态')
    default_address = models.ForeignKey('Address', related_name='users', null=True, blank=True,
                                        on_delete=models.SET_NULL, verbose_name='默认地址')

    class Meta:
        db_table = 'tb_users'
        verbose_name = "用户"
        verbose_name_plural = verbose_name


class AddressManager(models.Manager):
    '''地址模型管理器类'''
    # 1.改变原有查询的结果集:all()
    # 2.封装方法:用户操作模型类对应的数据表(增删改查)
    def get_default_address(self, user):
        '''获取用户默认收货地址'''
        # self.model:获取self对象所在的模型类
        try:
            address = self.get(user=user, is_default=True)  # models.Manager
        except self.model.DoesNotExist:
            # 不存在默认收货地址
            address = None

        return address


class Address(BaseModel):
    """
    用户地址
    """
    TIME_CHOICES = (
        ('am', '上午08点-12点'),
        ('pm', '下午12点-18点'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', verbose_name='用户')
    # title = models.CharField(max_length=20, verbose_name='地址名称')
    receiver = models.CharField(max_length=20, verbose_name='收货人')
    # province = models.ForeignKey('Area', on_delete=models.PROTECT, related_name='province_addresses',
    #                              verbose_name='省')
    # city = models.ForeignKey('areas.City', on_delete=models.PROTECT, related_name='city_addresses', verbose_name='市')
    province = models.ForeignKey('areas.Area', on_delete=models.PROTECT, related_name='province_addresses',
                                 verbose_name='省', default=None)
    city = models.ForeignKey('areas.Area', on_delete=models.PROTECT, related_name='city_addresses', verbose_name='市',
                             default=None)
    district = models.ForeignKey('areas.Area', on_delete=models.PROTECT, related_name='district_addresses',
                                 verbose_name='区', default=None)
    place = models.CharField(max_length=50, verbose_name='地址')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    zip_code = models.CharField(max_length=10, verbose_name='邮编', default=100000)
    landmark = models.CharField(max_length=20, null=True, blank=True, verbose_name='标志建筑')
    best_send_time = models.CharField(choices=TIME_CHOICES, max_length=15,
                                      verbose_name='最佳配送时间')
    tel = models.CharField(max_length=20, null=True, blank=True, default='', verbose_name='固定电话')
    email = models.CharField(max_length=30, null=True, blank=True, default='', verbose_name='电子邮箱')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')
    is_deleted = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_address'
        verbose_name = '用户地址'
        verbose_name_plural = verbose_name
        ordering = ['-update_time']

    def __str__(self):
        return self.user.username


class Message(BaseModel):
    '''留言'''
    MSG_TYPE = (
        (1, '留言'),
        (2, '投诉'),
        (3, '询问'),
        (4, '售后'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    type = models.SmallIntegerField(choices=MSG_TYPE, verbose_name='留言类型')
    title = models.CharField(max_length=50, verbose_name='主题')
    content = models.TextField(max_length=200, verbose_name='留言内容')
    file = models.FileField(upload_to='user/file', null=True, blank=True, verbose_name='上传文件')

    class Meta:
        db_table = 'tb_message'
        verbose_name = '用户留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Packet(models.Model):
    PACKET_RULE = (
        (1, '满减'),
        (2, '折扣'),
    )
    '''红包'''
    name = models.CharField(max_length=20, verbose_name='名称')
    rule = models.SmallIntegerField(choices=PACKET_RULE, verbose_name='规则')
    start_time = models.DateTimeField(auto_now_add=True, verbose_name='起始时间')
    end_time = models.DateTimeField(auto_now_add=True, verbose_name='结束时间')
    is_active = models.BooleanField(default=False, verbose_name='是否启用')

    class Meta:
        db_table = 'tb_packet'
        verbose_name = '红包'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
