from django.shortcuts import render
from .models import Product


def menu(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'menu/menu.html', context=context)