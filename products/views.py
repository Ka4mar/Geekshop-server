import datetime
import os
import json

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
    }
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context['products'] = json.load(open(file_path, encoding='utf-8 '))

    return render(request, 'products/products.html', context)
