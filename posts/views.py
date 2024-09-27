from django.shortcuts import render
from .forms import PostForm

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

    context = {
        "form": form,
    }

    return render(request, 'posts/create_post.html', context)
