"""
Context processor for shopping cart items
"""
import math
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_products = []
    total = 0
    delivery = round(Decimal(settings.DELIVERY_COST/100), 2)
    product_count = 0

    cart = request.session.get("cart", {})

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        if product.sale:
            individual_cost = round(Decimal((product.price * product.sale) * quantity), 2)
        else:
            individual_cost = round(Decimal(product.price * quantity), 2)
        total += individual_cost
        
        if "coffee" in product.tags:
            max_qty = math.floor(product.stock/250)
        else:
            max_qty = product.stock

        product_count += quantity

        cart_products.append({
            "product_id": product.id,
            "quantity": quantity,
            "individual_cost": individual_cost,
            "product": product,
            "max_qty": max_qty
        })
    
    total_delivered = total + delivery

    context = {
        "cart_products": cart_products,
        "total": total,
        "delivery": delivery,
        "total_delivered": total_delivered,
        "product_count": product_count,
    }

    return context