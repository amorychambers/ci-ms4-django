"""
Context processor for shopping cart items
"""

from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):

    cart_products = []
    total = 0
    product_count = 0

    cart = request.session.get("cart", {})

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        if product.sale:
            individual_cost = (product.price * product.sale) * quantity
        else:
            individual_cost = product.price * quantity
        total += individual_cost
        
        product_count += quantity

        cart_products.append({
            "product_id": product.id,
            "quantity": quantity,
            "individual_cost": individual_cost,
            "product": product
        })

    context = {
        "cart_products": cart_products,
        "total": total,
        "product_count": product_count
    }

    return context