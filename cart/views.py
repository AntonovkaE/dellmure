from my_shop.models import Product, Category, Size
from cart.cart import Cart
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request):
    size_id = request.POST.get('size')
    product = get_object_or_404(Size, id=size_id)
    cart = Cart(request)
    cart.add(product=product,
            quantity=1,
            update_quantity=False)
    return redirect('cart_detail')

def cart_remove(request, size_id):
    cart = Cart(request)
    product = get_object_or_404(Size, id=size_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})