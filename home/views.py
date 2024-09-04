from django.shortcuts import render

# Create your views here.

def index(request):
    """
    View returns index homepage
    """
    return render(request, 'home/index.html')