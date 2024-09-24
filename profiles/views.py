from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm

# Create your views here.

def profile(request):
    """
    Display user profile
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Delivery Information updated!')

    form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    context = {
        'user_profile': user_profile,
        'form': form,
        'orders': orders,
    }
    return render(request, 'profiles/profile.html', context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, f"Order placed on {order.date}")
    context = {
        'order': order,
        'from_profile': True
    }

    return render(request, 'checkout/checkout_success.html', context)