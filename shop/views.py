from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Product, Category


def index(request):
    latest_product_list = Product.objects.order_by('-pub_date')[:8]
    context = {'latest_product_list': latest_product_list}
    
    return render(request, 'shop/index.html', context)

def product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except:
        raise Http404("we don't have such an item:(")
    context = {'product': product}
    return render(request, 'shop/product.html', context)

def category(request, category_id):
    try:
        products_list = Product.objects.filter(category=category_id)
        category = Category.objects.get(id=category_id)
    except:
        raise Http404("we don't have such an category:(")
    context = {'products_list': products_list,
               'category': category}
    return render(request, 'shop/category.html', context)