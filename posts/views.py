from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import PostForm
from .models import Post

import math

from products.models import Product

# Create your views here.


def posts(request):
    """
    View to render all community posts
    """

    # Paginator code snippet taken from django documentation
    posts = Post.objects.all().order_by('id').reverse()
    paginator = Paginator(posts, 3)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }

    return render(request, 'posts/posts.html', context)


@login_required
def create_post(request):
    """
    View to submit new community post
    """

    user = get_object_or_404(User, username=request.user)

    form = PostForm()
    form.fields['product'].queryset = Product.objects.filter(
        tags__contains="coffee")

    if request.method == "POST":
        post = Post.objects.create(
            user=user)
        form = PostForm(request.POST, request.FILES,
                        instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Check out your post in \
                             the community tab!')
            return redirect(reverse('posts'))
        else:
            messages.error(request, 'Something went wrong! Please check \
                           that you included a title and content.')
            return redirect(reverse('create_post'))

    context = {
        "form": form,
    }

    return render(request, 'posts/create_post.html', context)


@login_required
def update_post(request, post_id):
    """
    View to update posts
    """

    user = get_object_or_404(User, username=request.user)
    post = get_object_or_404(Post, pk=post_id)

    if user == post.user:
        form = PostForm(instance=post)
        form.fields['product'].queryset = Product.objects.filter(
        tags__contains="coffee")

        if request.method == "POST":
            if user == post.user:
                form = PostForm(request.POST, request.FILES,
                                instance=post)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Check out your post in \
                                    the community tab!')
                    return redirect(reverse('posts'))
                else:
                    messages.error(request, 'Something went wrong! Please check \
                                that you included a title and content.')
                    return redirect(reverse('create_post'))
            else:
                messages.error(request, 'Sorry, only the original poster\
                            can make changes to the post.')
                return redirect(reverse('posts'))

        context = {
            "post": post,
            "form": form,
        }

        return render(request, 'posts/update_post.html', context)
    else:
        messages.error(request, 'Sorry, only the original poster\
                            can make changes to the post.')
        return redirect(reverse('posts'))



@login_required
def delete_post(request, post_id):
    """
    View to delete community posts
    """

    post = get_object_or_404(Post, pk=post_id)

    if request.user == post.user:
        post.delete()
        messages.success(request, 'Post deleted!')
    else:
        messages.error(request, 'Sorry, only the post owner can do that.')
    return redirect(reverse('posts'))
