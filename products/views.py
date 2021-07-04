import datetime
import os
import json

from products.models import Product, ProductCategory
from django.shortcuts import render

# Create your views here.
# Функции = контроллер = вьюхи

MODULE_DIR = os.path.dirname(__file__)


def index(request):
    date = datetime.datetime.now()
    context = {
        'title': 'geek Shop',
        'date': date,
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }

    return render(request, 'products/products.html', context)


