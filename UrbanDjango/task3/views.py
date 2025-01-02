from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def main_page_f(request):
    return render(request, 'third_task/main_page.html')


def shop_page_f(request):
    return render(request, 'third_task/shop_page.html')


def cart_page_f(request):
    return render(request, 'third_task/cart_page.html')