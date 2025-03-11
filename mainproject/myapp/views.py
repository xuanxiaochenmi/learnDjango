from django.shortcuts import render
from django.db import models
from .models import cal
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def CalPage(request):
    return render(request,'cal.html')

def CalAdd(request):
    if request.method == 'POST':
        value_a = int(request.POST['valueA'])
        value_b = int(request.POST['valueB'])
        result = value_a + value_b
        # 将数据写入数据库
        cal.objects.create(value_a=value_a,value_b=value_b,result=value_a+value_b)
        print(value_a,value_b , value_a+value_b)
        return render(request,'result.html',context={'data' : result})
    else:
        return HttpResponse('please visit us with post')

def CalList(request):
    data = cal.objects.all()
    #for each in data:
        #print(each.value_a,each.value_b,each.result)
    return render(request,'list.html',context={'data':data})

def DelData(request):
    cal.objects.all().delete()

    return HttpResponse('DATA DELETED')