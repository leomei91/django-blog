# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from web.models import *
# Register your models here.
#admin.site.register([Test,Contact,Tag])
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email') 
    search_fields = ('name',)

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test,Article])
