# posts/urls.py
app_name = 'posts' # переменная app_name, в которой тоже указывается namespace для путей приложения
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
] 
# из пространства имён namespace='posts' получить адрес из path() с name='index'».
# Больше конфликтов не будет: namespace уверенно укажет, к какому именно path() нужно обратиться, даже если name приложений дублируются.
