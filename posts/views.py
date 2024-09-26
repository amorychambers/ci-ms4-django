from django.shortcuts import render

# Create your views here.

def posts(request):
    """
    View to render all community posts
    """

    return render(request, 'posts/posts.html')