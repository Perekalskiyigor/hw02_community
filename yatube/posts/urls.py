# posts/urls.py
from django.urls import path
from . import views
app_name = 'posts'  # переменная app_name, в которой  указся namespace для пут

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
]
# из пространства имён namespace='posts' получ адрес из path() с name='index'».
