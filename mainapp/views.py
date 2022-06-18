import datetime

from django.shortcuts import render
from .models import HabrCategory, Habr
from django.core.paginator import Paginator


def main(request):
    title = {
        "page_title": "Главная",
        "title_row_1": "ДОБРО ПОЖАЛОВАТЬ НА ПОРТАЛ",
        "title_row_2": "Наш Хабр"
    }

    habr = [
        {
            "name": "Новости из мира IT",
            "desc": "Новости из мира IT со всего мира",
            "image_src": "",
            "image_href": "",
            "alt": "...",
        },
        {
            "name": "Новости со всего мира",
            "desc": "Не оторваться.",
            "image_src": "",
            "image_href": "",
            "alt": "...",
        },
    ]
    content = {"title": title, "habr": habr}
    return render(request, "mainapp/index.html", content)


def habr(request):
    title = {
        "page_title": "Главная",
        "title_row_1": "Наш Хабр",
        "title_row_2": "Дизайн"
    }
    same_habr = [
        {"name": "Отличная новость", "desc": "Не оторваться.", "image_src": "", "alt": "..."},
        {"name": "Свежая новость", "desc": "То-то еще будет", "image_src": "", "alt": "..."},
        {
            "name": "Новости для хакинга",
            "desc": "Просто попробуйте.",
            "image_src": "",
            "alt": "...",
        },
    ]
    content = {"title": title, "same_habr": same_habr}
    return render(request, "mainapp/blog_list.html", content)


def help(request):
    title = "о нас"
    visit_date = datetime.datetime.now()
    locations = [
        {
            "city": "Moscow",
            "phone": "+7-495-777-7777",
            "email": "info_habr@geekbrains.ru",
            "address": "Близко к центру",
        },
    ]
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/help.html", content)

# def index(request):
#     articles = Habr.objects.all()
#     categories = HabrCategory.objects.all()
#     return render(request, 'mainapp/index.html', context={'articles': articles,
#                                                           'categories': categories})

def get_category(request, category_id):
    articles = Habr.objects.filter(category_id=category_id)
    categories = HabrCategory.objects.all()
    paginator = Paginator(articles, 3)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    category = HabrCategory.objects.get(pk=category_id)
    return render(request, template_name='mainapp/category.html', context={'page_obj': page_objects,
                                                                           'articles': articles,
                                                                           'categories': categories,
                                                                           'category': category})

def index(request):
    articles = Habr.objects.all()
    categories = HabrCategory.objects.all()
    paginator = Paginator(articles, 3)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, template_name='mainapp/test.html', context={'page_obj': page_objects,
                                                                       'categories': categories})
