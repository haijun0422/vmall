from django.db import models


# class Province(models.Model):
#     province = models.CharField(max_length=10, verbose_name='省')
#
#     class Meta:
#         db_table = 'tb_province'
#         verbose_name = '省'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.province
#
#
# class City(models.Model):
#     city = models.CharField(max_length=10, verbose_name='市')
#     pid = models.ForeignKey(Province, verbose_name='省',null=True, blank=True, on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'tb_city'
#         verbose_name = '市'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.city

class Area(models.Model):
    atitle = models.CharField(max_length=20, verbose_name='城市', null=True, blank=True)
    aParent = models.ForeignKey('self',null=True, blank=True, on_delete=models.CASCADE, verbose_name='父级城市')

    class Meta:
        db_table = 'tb_area'
        verbose_name = '地区'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.atitle
    #
    # def title(self):
    #     return self.atitle
    #
    # title.admin_order_field = 'atitle'
    # title.short_description = '地区名称'
    #
    # def parent(self):
    #     if self.aParent is None:
    #         return ''
    #     return self.aParent.atitle
    #
    # parent.short_description = '父级地区名称'
