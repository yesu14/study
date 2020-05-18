from django.db import models


# Create your models here.


class history(models.Model):
    item_name = models.CharField(max_length=32,null=True)
    item_price = models.CharField(max_length=32,null=True)
    user_id = models.ForeignKey("UserInfo",to_field="id",default=1)

class UserInfo(models.Model):
    username = models.CharField(max_length=32,null=True)
    password = models.CharField(max_length=64)
    user_type = (
        (1,'超级用户'),
        (2,'普通用户'),
        (3,'管理员'),
    )
    user_type_id = models.IntegerField(choices=user_type,null=True)
    create_time = models.DateTimeField(auto_now=True,null=True)
    upadate_time = models.DateTimeField(auto_now_add=True,null=True)
    # age = models.IntegerField()
