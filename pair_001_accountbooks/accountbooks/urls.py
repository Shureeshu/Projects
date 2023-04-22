from django.urls import path
from . import views

app_name="accountbooks"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:account_book_pk>/', views.detail, name="detail"),
    path('new/', views.create, name="create"),
]   