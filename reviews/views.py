from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Review
from .forms import ReviewForm

# Create your views here.

@login_required
def review(request, product_id):
    """
    View to create new reviews
    """
    user = get_object_or_404(User, username=request.user)
    product = get_object_or_404(Product, id=product_id)
    try:
        review = Review.objects.get(
            user = user,
            review_product = product
        )
        form = ReviewForm(instance=review)
    except Review.DoesNotExist:
        review = Review.objects.create(
            user=user,
            review_product=product
            )
        form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid() and int(
            request.POST.get('user')) == request.user.id:
            form.save()
            messages.success(request, 'Thanks for leaving a review! \
                              We appreciate all feedback.')
            return redirect(reverse('product_details',
                                     kwargs={'product_id':product_id}))
        else:
            messages.error(request, 'Something went wrong! Please check \
                           that you completed both parts of the review.')
            return redirect(reverse('review',
                                     kwargs={'product_id':product_id}))

    context = {
        'user': user,
        'product': product,
        'form': form,
    }
    return render(request, 'reviews/review.html', context)

@login_required
def delete_review(request, review_id):
    """
    View to delete reviews
    """

    review = get_object_or_404(Review, pk=review_id)
    product = review.review_product.id

    if request.user == review.user:
        review.delete()
        messages.success(request, 'Review deleted!')
    else:
        messages.error(request, 'Sorry, only the review owner can do that.')
    return redirect(reverse('product_details', kwargs={"product_id":product}))