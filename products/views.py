from django.shortcuts import render
from django.db.models import Q
from .models import Product

# Create your views here.

def products(request):
    """
    View to display and sort all products
    """

    products = Product.objects.all()
    sort = None

    if request.GET:
        sort = request.GET["sort"]
        if sort == "sale":
            products = Product.objects.filter(Q(sale__gt=0))
        else:
            products = Product.objects.filter(Q(tags__contains=sort))

    context = {
        "products": products,
        "sort": sort,
    }
    
    return render(request, 'products/products.html', context)