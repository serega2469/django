from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, re_path
from django.template.loader import render_to_string
from .models import Women, Category


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.

Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
     'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def index(request):
    posts = Women.published.all()
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': posts,
            'cat_selected': 0,

    }
    return render(request, 'index.html', context=data)


def about(request):
    return render(request, 'about.html', {'title': 'О сайте', 'menu': menu})


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


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'post.html', data)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return render(request, 'contact.html')


def login(request):
    return HttpResponse("Авторизация")


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk)
    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }

    return render(request, 'women/index.html', context=data)


