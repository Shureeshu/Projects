from django.shortcuts import render, redirect
from .models import AccountBook

# Create your views here.
def index(request):
    context = {
        'accountbooks': AccountBook.objects.all().order_by('-date')
    }
    return render(request, 'accountbooks/index.html', context)

def detail(request, account_book_pk):
    item = AccountBook.objects.get(pk=account_book_pk)
    return render(request, 'accountbooks/detail.html', {'item':item})

def create(request):
    if request.method == "POST":
        AccountBook.objects.create(note=request.POST['note'], category=request.POST['category'], date=request.POST['date'])
        return redirect('accountbooks:index')
    else:
        context = {
            'category_list': AccountBook.CATEGORY
        }
        return render(request, 'accountbooks/create.html', context)

