from django.shortcuts import render
from .forms import PostForm
from products.models import Product

# Create your views here.

def posts(request):
    """
    View to render all community posts
    """
    return render(request, 'posts/posts.html', )


def create_post(request):
    """
    View to submit new community post
    """

    form = PostForm()
    form.fields['product'].queryset = Product.objects.filter(
        tags__contains="coffee")

    context = {
        "form": form,
    }

    return render(request, 'posts/create_post.html', context)
