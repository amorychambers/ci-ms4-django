from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PostForm
from .models import Post
from products.models import Product

# Create your views here.

def posts(request):
    """
    View to render all community posts
    """
    return render(request, 'posts/posts.html', )

@login_required
def create_post(request):
    """
    View to submit new community post
    """

    form = PostForm()
    form.fields['product'].queryset = Product.objects.filter(
        tags__contains="coffee")
    
    if request.method == "POST":
        post = Post.objects.create(
            user=request.user,
        )
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Check out your post in \
                             the community tab!')
            return redirect(reverse('posts'))
        else:
            messages.error(request, 'Something went wrong! Please check \
                           that you included a title and content.')
            return redirect(reverse('create_post',
                                     kwargs={'form':form}))

    context = {
        "form": form,
    }

    return render(request, 'posts/create_post.html', context)
