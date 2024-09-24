from django.shortcuts import render

# Create your views here.

def profile(request):
    """
    Display user profile
    """
    context = {}
    return render(request, 'profiles/profile.html', context)