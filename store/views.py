# pylint: disable=no-member
from django.shortcuts import render

from .models import Order, Product


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

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    """
    checkout view
    """
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        # empty cart for non logged in users
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        items = []
    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)
