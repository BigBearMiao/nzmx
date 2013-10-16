# -*- coding: utf-8 -*-
from django.db import models


class Customer(models.Model):
    GENDER_CHOICES=(
                    ("M","男"),
                    ("F","女")
                    )
    cust_name = models.CharField('姓名',max_length=15,blank=False)
    gender = models.CharField('性别',max_length=1,choices=GENDER_CHOICES)
    age = models.IntegerField('年龄')
    money = models.DecimalField('余额',default=0.00,max_digits=9,decimal_places=2,blank=False)
    phone = models.CharField('手机',max_length=15,blank=False)
    weight = models.DecimalField('体重',max_digits=5,decimal_places=2,blank=True)
    create_date = models.DateField('创建日期',auto_now_add=True)
    last_update = models.DateField(auto_now=True)
    memo = models.CharField('备注',max_length=50,blank=True)
    memlevel = models.ForeignKey('MemberLevel',verbose_name='会员级别')
    
    class Meta:
        verbose_name = '会员'
        verbose_name_plural='会员'
    
    def __unicode__(self):
        return u'%s' % self.cust_name


class MemberLevel(models.Model):
    level_name = models.CharField(max_length=12,blank=False)
    base_price = models.IntegerField(default=0)
    service_discount = models.DecimalField(default=0.00,max_digits=3, decimal_places=2,blank=False)
    product_discount = models.DecimalField(default=0.00,max_digits=3,decimal_places=2,blank=False)
    memo = models.CharField(max_length=20)
    
    def __unicode__(self):
        return u'%s' % self.level_name
    


    

