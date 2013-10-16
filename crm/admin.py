'''
Created on 2013-10-16

@author: huzx
'''
from django.contrib import admin
from crm.models import Customer,MemberLevel

admin.site.register(Customer)
admin.site.register(MemberLevel)