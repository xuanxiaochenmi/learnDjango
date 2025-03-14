"""
URL configuration for mainproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.http import HttpResponse  # 如果需要简单测试

def home(request):
    return HttpResponse("欢迎来到首页！")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('CalPage/', views.CalPage),
    path('cal/', views.CalAdd),
    path('list/', views.CalList),
    path('del/',views.DelData)]
