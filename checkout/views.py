from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Based on Code Institue's "Boutique Ado" Walkthrough Project

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "The shopping cart is empty at the moment")
        return redirect(reverse('books'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
