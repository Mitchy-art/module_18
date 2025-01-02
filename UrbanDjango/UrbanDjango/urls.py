"""
URL configuration for UrbanDjango project.

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
# from task2.views import index
# from task2.views import func_tem
# from task2.views import Class_tem
from task3.views import main_page_f
from task3.views import shop_page_f
from task3.views import cart_page_f

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),
    # path('func/', func_tem),
    # path('class/', Class_tem.as_view()),
    path('', main_page_f),
    path('main_page/shop_page/', shop_page_f),
    path('main_page/cart_page/', cart_page_f),
]
