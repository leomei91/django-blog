# -*- coding: utf-8 -*-

from django.http import HttpResponse

from web.models import Test

# 数据库操作
def testdb(request):

  test1 = Test.objects.get(id=1)  
  test1.name = "zhangsan"
  test1.save()
  response = ""
  response1 = ""
  list = Test.objects.all()
  for var in list:
      response1 += var.name + " "
      response2 = var.age
      r1 = response1
      r2 = response2
      r = r1 + str(r2)
      return HttpResponse(r1)
