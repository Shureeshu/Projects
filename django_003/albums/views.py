from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm


# Create your views here.
def index(request):
    
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        form.save()
    else:
        pass
    context = {
        'albums': Album.objects.all(),
        'form': AlbumForm(),
    }

    return render(request, 'albums/index.html', context)

