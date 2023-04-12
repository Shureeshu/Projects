# reviews/models.py
from django.db import models

# Create your models here.
# django ForeignKey 필드를 사용하여 Many-to-One 관계 생성.

class Review(models.Model):
# 앱 이름 : reviews
# 모델 이름 : Review

# title	리뷰 제목
# content	리뷰 내용
# movie	영화 제목
    title = models.CharField(max_length=80) 
    content = models.TextField()  
    movie = models.CharField(max_length=80)
    

class Comment(models.Model):
# 앱 이름 : reviews
# 모델 이름 : Comment

# review	댓글 작성 리뷰	ForeignKey	Review, on_delete=models.CASCADE
# content	댓글 내용
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
