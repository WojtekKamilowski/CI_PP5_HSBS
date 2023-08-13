# 3rd Party imports
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Internal imports
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


# Based on Code Institue's "Boutique Ado" Walkthrough Project


@login_required
def profile(request):
    """
    Displays profile of the user
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile has been updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid & try again.'))
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'Confirmation for previous order number: {order_number}. '
        'We sent you a confirmation email on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
