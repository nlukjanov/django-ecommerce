# pylint: disable=no-member
from django.shortcuts import render
from .models import *


def store(request):
    """
    store view
    """
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)


def cart(request):
    """
    cart view
    """
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    """
    checkout view
    """
    context = {}
    return render(request, 'store/checkout.html', context)
