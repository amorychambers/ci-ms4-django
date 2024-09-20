from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from cart.contexts import cart_contents
from decimal import Decimal

import stripe

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "There's nothing in the shopping cart")
        return redirect(reverse("products"))
    
    current_cart = cart_contents(request)

    if 'delivery' in request.GET:
        total = current_cart['total']
    else:
        total = current_cart['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
    
    order_form = OrderForm()
    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)