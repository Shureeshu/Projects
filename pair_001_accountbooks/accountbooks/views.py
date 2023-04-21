from django.shortcuts import render
from .models import AccountBook

# Create your views here.
def index(request):
    context = {
        'accountbooks': AccountBook.objects.all()
    }
    return render(request, 'accountbooks/index.html', context)