from django.shortcuts import render

# Create your views here.

def index(request):
    """
    View to return homepage
    """
    return render(request, 'home/index.html')


def contact(request):
    """
    View to return and handle contact form,
    with about us info
    """

    return render(request, 'home/contact.html')