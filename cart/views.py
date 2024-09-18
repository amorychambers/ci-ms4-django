from django.shortcuts import render, redirect, reverse, HttpResponse

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

    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")

    cart = request.session.get("cart", {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    request.session["cart"] = cart

    return redirect(redirect_url)


def update_cart(request, product_id):
    """
    View to update quantities of products from the shopping cart page
    """

    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart")

    if quantity > 0:
        cart[product_id] = quantity
    else:
        cart.pop(product_id)

    request.session["cart"] = cart

    return redirect(reverse("cart"))


def remove_from_cart(request, product_id):
    """
    View to remove an item from the shopping cart
    """
    try:
        cart = request.session.get("cart")

        cart.pop(product_id)

        request.session["cart"] = cart
        return HttpResponse(status=200)
    
    except Exception as e:
        return HttpResponse(status=500)