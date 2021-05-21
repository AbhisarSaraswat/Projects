from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Images
from django.db.models import Q

def home(request):
    categories_model = Product.objects.values_list('type').distinct()
    categories = []
    for i in categories_model:
        categories.append(i[0])
    print(categories)
    return render(request, 'products/home.html', {'categories':categories})

def detail(request, product_id):
    # print(product_id)
    product = get_object_or_404(Product,pk=product_id)
    photos = Images.objects.filter(product=product)

    print(photos)
    return render(request, 'products/detail.html', {'product':product,'photos':photos})


def category(request, type):
    product = Product.objects.filter(type=type).values()
    photos = Images.objects.filter(product=product)
    print(product)
    return render(request, 'products/category.html', {'product':product,'photos':photos})