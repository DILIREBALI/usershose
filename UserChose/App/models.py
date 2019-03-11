from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户姓名')
    userphone = models.CharField(max_length=16, unique=True, verbose_name='手机号')

class Chose(models.Model):
    color = models.CharField(max_length=12, verbose_name='鞋子颜色')
    size = models.CharField(max_length=8, verbose_name='鞋子大小')
    user = models.ForeignKey(User)
