from django.db import models
from utils.db_models import BaseModel


class OAuthUser(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    openid = models.CharField(db_index=True, max_length=64)

    class Meta:
        db_table = 'tb_oauth'
        verbose_name = 'QQ用户'
        verbose_name_plural = verbose_name
