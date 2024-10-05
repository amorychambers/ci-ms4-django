from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Product
from .forms import ProductForm
from reviews.models import Review
import math

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
    reviews = Review.objects.filter(
        Q(review_product=product.id)).order_by('-date')

    if "coffee" in product.tags and "bundle" not in product.tags:
        max_qty = math.floor(product.stock/250)
    else:
        max_qty = product.stock

    context = {
        "product": product,
        "max_qty": max_qty,
        "reviews": reviews,
    }

    return render(request, "products/product_details.html", context)


# Code snippet customised from Code Institute Boutique Ado project
@login_required
def add_product(request):
    """
    View to add products
    """
    if not request.user.is_superuser:
        messages.error(request, 'You must be logged in to a store owner \
                       account to do this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                           Please ensure the form is valid.')
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'products/add_product.html', context)


@login_required
def update_product(request, product_id):
    """
    View to update products
    """
    if not request.user.is_superuser:
        messages.error(request, 'You must be logged in to a store owner \
                       account to do this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, id=product_id)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product updated!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                           Please ensure the form is valid.')

    context = {
        "product": product,
        "form": form,
    }

    return render(request, 'products/update_product.html', context)
