from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def cart(request):
    """
    View to render the shopping cart
    """

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """
    View to add a new item to the shopping cart
    """

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")

    cart = request.session.get("cart", {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
        messages.success(request,
                         f"Added {quantity} x '{product.name}' \
                            to your shopping cart", extra_tags="view-cart")
    else:
        cart[product_id] = quantity
        messages.success(request,
                         f"Added {quantity} x '{product.name}' \
                            to your shopping cart", extra_tags="view_cart")

    request.session["cart"] = cart

    return redirect(redirect_url)


def update_cart(request, product_id):
    """
    View to update quantities of products from the shopping cart page
    """
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart")

    if quantity > 0:
        cart[product_id] = quantity
        messages.success(request,
                         f"Updated {product.name} quantity to {quantity}",
                         extra_tags="view_cart")
    else:
        cart.pop(product_id)
        messages.success(request,
                         f"{product.name} removed from cart",
                         extra_tags="view_cart")

    request.session["cart"] = cart

    return redirect(reverse("cart"))


def remove_from_cart(request, product_id):
    """
    View to remove an item from the shopping cart
    """
    product = get_object_or_404(Product, pk=product_id)

    try:
        cart = request.session.get("cart")

        cart.pop(product_id)

        request.session["cart"] = cart
        messages.success(request, f"{product.name} removed from cart",
                         extra_tags="view_cart")
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
