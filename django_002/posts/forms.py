# posts/forms.py

# 폼 이름 : PostForm
# 폼 모델 : Post
# 입력 필드
# title
# content
# category

from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category',)
