import datetime
import os
from django.conf import settings
from django.core.cache import cache
from products.models import Product, ProductCategory
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.cache import cache_page

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


def get_products():
    if settings.LOW_CACH:
        key = 'products_list'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = Product.objects.all()
            cache.set(key, links_menu)
        return links_menu
    else:
        return Product.objects.all()


@cache_page(3600)
def products(request, category_id=None, page=1):

    context = {'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id).select_related()
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator
    return render(request, 'products/products.html', context)












