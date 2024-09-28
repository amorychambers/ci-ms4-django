from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

# Create your views here.

@login_required
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

@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    context = {
        'order': order,
        'from_profile': True
    }
    if request.user == order.user_profile.user:
        messages.info(request, f"Order placed on {order.date}")
        return render(request, 'checkout/checkout_success.html', context)
    else:
        messages.error(request, 'Sorry, only the user who made the \
                       order can view it. If you believe this \
                       order should be associated with your profile, \
                       please contact us.')
        return redirect(reverse('home'))
    

@login_required
def delete_account(request):
    """
    View to delete user account
    """

    user = get_object_or_404(User, pk=request.user.id)
    user.delete()
    messages.info(request, 'Account deleted. Goodnight and good luck!')
    return redirect('home')

