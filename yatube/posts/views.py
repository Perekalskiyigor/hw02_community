# from django.shortcuts import render
from re import template
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group

# Create your views here.

# Главная страница
def index(request): 
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    # title = 'Это главная страница проекта Yatube'   
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
         'posts': posts,
    }
    return render (request, template, context)



def group_posts(request, slug):
    print("начало функции") 
    # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    template = 'posts/group_list.html'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context) 