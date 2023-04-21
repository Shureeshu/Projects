from django.shortcuts import render
from .models import AccountBook

# Create your views here.
def index(request):
    context = {
        'accountbooks': AccountBook.objects.all()
    }
    return render(request, 'accountbooks/index.html', context)

"""
GET account-books/<int:account_book_pk>/
pk가 account_book_pk인 데이터 조회
조회한 데이터를 전달한 단일 조회 템플릿 렌더링
view에서 전달받은 데이터 출력
수정, 삭제, 복사 버튼
"""

def detail(request, account_book_pk):
    item = AccountBook.objects.get(pk=account_book_pk)
    return render(request, 'accountbooks/detail.html', {'item':item})