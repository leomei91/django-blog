# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test(models.Model):
	name = models.CharField(max_length=20)
	age = models.IntegerField(default=20)

class Contact(models.Model):
    name   = models.CharField(max_length=200)
    age    = models.IntegerField(default=0)
    email  = models.EmailField()
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    contact = models.ForeignKey(Contact)
    name    = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
class Article(models.Model):
    title   = models.CharField('标题',max_length=200)
    name    = models.CharField('姓名',max_length=200)
    text  = models.TextField('正文',)
    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '文章'
    def __unicode__(self):
        return self.name

