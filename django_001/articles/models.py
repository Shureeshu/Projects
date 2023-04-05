# articles/models.py 

from django.db import models

# Create your models here.
class Article(models.Model):
  # id 필드는 자동 생성
  title = models.CharField(max_length=10)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

