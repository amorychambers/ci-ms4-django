from django.shortcuts import render

# Create your views here.

def cart(request):
    """
    View to render the shopping cart
    """

    return render(request, 'cart/cart.html')