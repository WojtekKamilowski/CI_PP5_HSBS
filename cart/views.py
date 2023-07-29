from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from books.models import Book

# Based on Code Institue's "Boutique Ado" Walkthrough Project


def view_cart(request):
    """
    Renders the cart
    """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Adds books to the to shopping cart
    """

    book = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request,
                         (f'Updated {book.name} '
                          f'quantity to {cart[item_id]}'))
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {book.name} to your shopping cart')

    request.session['cart'] = cart
    return redirect(redirect_url)
