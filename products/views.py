from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product

# Create your views here.

def products(request):
    """
    View to display and sort all products
    """

    products = Product.objects.all()
    sort = None
    search = None

    if request.GET:
        if "sort" in request.GET:
            sort = request.GET["sort"]
            if sort == "sale":
                products = Product.objects.filter(Q(sale__gt=0))
            else:
                products = Product.objects.filter(Q(tags__contains=sort))
            if sort == "single":
                sort = "Single Origin"
            if sort == "bundle":
                sort = "Bundles"

        if "search" in request.GET:
            search = request.GET["search"]
            products = Product.objects.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
                )

    

    context = {
        "products": products,
        "sort": sort,
        "search": search,
    }
    
    return render(request, "products/products.html", context)


def product_details(request, product_id):
    """
    View to display single product page
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "products/product_details.html", context)