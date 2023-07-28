from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from books.models import Book


def view_cart(request):
    """ 
    Renders the cart
    """

    return render(request, 'cart/cart.html')
