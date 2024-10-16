from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from products.models import Product
from .models import Order, OrderLineItem
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from .forms import OrderForm
from cart.contexts import cart_contents
from decimal import Decimal

import stripe
import json

# Create your views here.


# Code snippet for this view from Code Institute Boutique Ado project
@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        cart = request.session.get("cart", {})
        if request.POST['order_type'] == 'delivery':
            form_data = {
                'full_name': request.POST['full_name'],
                'email': request.POST['email'],
                'phone_number': request.POST['phone_number'],
                'postcode': request.POST['postcode'],
                'town_or_city': request.POST['town_or_city'],
                'street_address1': request.POST['street_address1'],
                'street_address2': request.POST['street_address2'],
                'county': request.POST['county'],
                'collection': False
            }
        else:
            form_data = {
                'full_name': request.POST['full_name'],
                'email': request.POST['email'],
                'collection': True
            }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for product_id, product_data in cart.items():
                try:
                    product = get_object_or_404(Product, id=product_id)
                    order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=product_data,
                        )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag \
                            wasn't found in our database. \
                                Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
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

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                if 'delivery' in request.GET:
                    order_form = OrderForm(initial={
                        'full_name': profile.user.get_full_name(),
                        'email': profile.user.email,
                        'phone_number': profile.default_phone_number,
                        'street_address1': profile.default_street_address1,
                        'street_address2': profile.default_street_address2,
                        'town_or_city': profile.default_town_or_city,
                        'county': profile.default_county,
                        'postcode': profile.default_postcode,
                        'collection': False
                    })
                else:
                    order_form = OrderForm(initial={
                        'full_name': profile.user.get_full_name(),
                        'email': profile.user.email,
                        'collection': True
                    })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        context = {
            "order_form": order_form,
            "order_for_delivery": order_for_delivery,
            "stripe_public_key": stripe_public_key,
            "client_secret": intent.client_secret,
        }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """
    View to communicate successful purchase to customer
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user == order.user_profile.user:
        for item in order.lineitems.all():
            product = get_object_or_404(Product, pk=item.product.id)
            if 'coffee' in product.tags:
                product.stock -= (item.quantity * 250)
            else:
                product.stock -= item.quantity
            product.save()

        if request.user.is_authenticated:
            user_profile = get_object_or_404(UserProfile, user=request.user)
            order.user_profile = user_profile
            order.save()

            if save_info:
                delivery_info = {
                    'default_phone_number': order.phone_number,
                    'default_street_address1': order.street_address1,
                    'default_street_address2': order.street_address2,
                    'default_town_or_city': order.town_or_city,
                    'default_county': order.county,
                    'default_postcode': order.postcode,
                }
                user_profile_form = UserProfileForm(
                    delivery_info, instance=user_profile)
                if user_profile_form.is_valid():
                    user_profile_form.save()

        messages.success(request, f'Order successful!\
                        Your order number is {order_number}.\
                            A confirmation email will be sent to {order.email}')

        if 'cart' in request.session:
            del request.session['cart']

        context = {
            'order': order,
        }

        return render(request, "checkout/checkout_success.html", context)
    else:
        messages.error(request, 'Sorry, only the user who made the \
                       order can view it. If you believe this \
                       order should be associated with your profile, \
                       please contact us.')
        return redirect(reverse('home'))
