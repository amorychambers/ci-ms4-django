from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from products.models import Product

# Create your views here.

def review(request, product_id):
    """
    View to create new reviews
    """
    if user.is_authenticated:
        user = get_object_or_404(User, username=request.user)
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'reviews/review.html')
    else:
        messages.error(request, "Sorry! You can only review \
                       products while signed in.")
        return redirect(reverse('product_details/{product_id}'))