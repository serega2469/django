from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, re_path
from django.template.loader import render_to_string

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': data_db,

    }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})


def categories(request, cat_id):
    return HttpResponse(f'<h1>Cтатьи по категориям</h1><p>id: {cat_id}</p>')


def archive(request, year):
    if year > 2023:
        redirect('home')
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Cтатьи по категориям</h1><p>id: {cat_slug}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


