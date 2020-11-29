from django.shortcuts import render


def store(request):
    """
    store view
    """
    context = {}
    return render(request, 'store/store.html', context)

def cart(request):
    """
    store view
    """
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    """
    store view
    """
    context = {}
    return render(request, 'store/checkout.html', context)
