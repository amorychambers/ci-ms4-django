from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.conf import settings
from products.models import Product
from .models import OrderLineItem
from .forms import OrderForm
from cart.contexts import cart_contents
from decimal import Decimal

import stripe

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        cart = request.session.get("cart", {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save()
            for product_id, product_data in cart.items():
                try:
                    product = Product.objects.get(id=product_id)
                    order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=product_data,
                        )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))
                
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your order. \
                           Please double check your information.')
    else:
        cart = request.session.get("cart", {})
        if not cart:
            messages.error(request, "There's nothing in the shopping cart")
            return redirect(reverse("products"))
        
        current_cart = cart_contents(request)

        if 'delivery' in request.GET:
            total = current_cart['total_delivered']
            order_for_delivery = True
        else:
            total = current_cart['total']
            order_for_delivery = False
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
            "order_for_delivery": order_for_delivery,
            "stripe_public_key": stripe_public_key,
            "client_secret": intent.client_secret,
        }

    return render(request, 'checkout/checkout.html', context)