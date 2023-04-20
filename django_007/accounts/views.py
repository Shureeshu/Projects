from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.
def profile(request):
    users = get_user_model().objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/profile.html', context)