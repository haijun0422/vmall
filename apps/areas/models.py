from django.db import models


class Province(models.Model):
    province = models.CharField(max_length=10, verbose_name='省')

    class Meta:
        db_table = 'tb_province'
        verbose_name = '省'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.province


class City(models.Model):
    city = models.CharField(max_length=10, verbose_name='市')
    pid = models.ForeignKey(Province, verbose_name='省',null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_city'
        verbose_name = '市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.city
