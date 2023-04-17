# reviews/views.py

from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

# Create your views here.


# 리뷰 전체 조회 - index GET
def index(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        context = {
            'reviews': reviews,
        }
        return render(request, 'reviews/index.html', context)
    else:
        return redirect('reviews:index', request(method="GET"))
    

# 리뷰 생성
def create(request):
    # POST ReviewForm 유효성 검사 통과시 데이터 생성
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews:index')
    form = ReviewForm()
    return render(request, 'reviews/create.html', {'form':form,})


# 리뷰 단일 조회 & 댓글 전체 조회
def detail(request, review_pk, comment_pk=None):
    
    review = Review.objects.get(pk=review_pk)
    empty_form = CommentForm()
    comments = review.comment_set.all()
    forms = [CommentForm(instance=comment) for comment in comments]
    
    # POST
    if request.method == "POST":
        if comment_pk == None:
            # create new comment
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.review = review
                form.save()
            
            return redirect('reviews:detail', review.pk)
        else:
            # delete comment
            comment = Comment.objects.get(pk = comment_pk)
            comment.delete()
        return redirect('reviews:detail', review.pk)
    
    context = {
        'empty_form': empty_form,
        'review':review,
        'forms':forms,
        'comments':comments,
    }
    return render(request, 'reviews/detail.html', context)
        

        
