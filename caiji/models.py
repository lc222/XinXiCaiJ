from __future__ import unicode_literals

# Create your models here.
# models.py
from django.db import models

class XinXiCaiJi(models.Model):
    xingming = models.CharField(max_length=20)
    xuehao = models.CharField(max_length=20)
    daoshi = models.CharField(max_length=20)
    dsdianhua = models.CharField(max_length=20)
    brdianhua = models.CharField(max_length=20)
    eMail = models.CharField(max_length=30)
    weixin = models.CharField(max_length=20)
    QQ = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    huochezhan = models.CharField(max_length=20)
    habit = models.CharField(max_length=400)
    money = models.CharField(max_length=20)
    baba = models.CharField(max_length=20)
    babaGongzuo = models.CharField(max_length=20)
    babatel = models.CharField(max_length=20)
    mama = models.CharField(max_length=20)
    mamaGongzuo = models.CharField(max_length=20)
    mamatel = models.CharField(max_length=20)
    hometel = models.CharField(max_length=20)
    homeadd = models.CharField(max_length=200)
    beijing = models.CharField(max_length=20)
    beijingGongzuo = models.CharField(max_length=20)
    beijingtel = models.CharField(max_length=20)
    dor = models.CharField(max_length=20)
    dorP = models.CharField(max_length=20)


