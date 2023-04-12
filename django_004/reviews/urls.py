# reviews/urls.py

from django.urls import path
from . import views

app_name = 'reviews'
urlpatterns = [
    
    # 리뷰 생성 - create GET, POST
    path("create", views.create, name="create"),
    # 리뷰 전체 조회 - index GET
    path("", views.index, name="index"),
    # 리뷰 단일 조회 & 댓글 전체 조회 - detail GET
    path("<int:review_pk>", views.detail, name = "detail"),
    # 댓글 생성 - detail POST
    path("<int:review_pk>/comments", views.detail, name = "comment"),
    # 댓글 삭제 - detail POST
    path("<int:review_pk>/comments/<int:comment_pk>/delete", views.detail, name = "delete_comment"),

]





     


