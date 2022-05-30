import datetime

from django.shortcuts import render


def main(request):
    title = "главная"
    habr = [
        {
            "name": "Отличный стул",
            "desc": "Расположитесь комфортно.",
            "image_src": "product-1.jpg",
            "image_href": "/product/1/",
            "alt": "продукт 1",
        },
        {
            "name": "Стул повышенного качества",
            "desc": "Не оторваться.",
            "image_src": "product-2.jpg",
            "image_href": "/product/2/",
            "alt": "продукт 2",
        },
    ]
    content = {"title": title, "habr": habr}
    return render(request, "mainapp/index.html", content)


def habr(request):
    title = "продукты"
    links_menu = [
        {"href": "habr_all", "name": "все"},
        {"href": "habr_home", "name": "дом"},
        {"href": "habr_office", "name": "офис"},
        {"href": "habr_modern", "name": "модерн"},
        {"href": "habr_classic", "name": "классика"},
    ]
    same_habr = [
        {"name": "Отличный стул", "desc": "Не оторваться.",
            "image_src": "product-11.jpg", "alt": "продукт 11"},
        {"name": "Стул повышенного качества", "desc": "Комфортно.",
            "image_src": "product-21.jpg", "alt": "продукт 21"},
        {
            "name": "Стул премиального качества",
            "desc": "Просто попробуйте.",
            "image_src": "product-31.jpg",
            "alt": "продукт 31",
        },
    ]
    content = {"title": title, "links_menu": links_menu,
               "same_habr": same_habr}
    return render(request, "mainapp/habr.html", content)


def help(request):
    title = "о нас"
    visit_date = datetime.datetime.now()
    locations = [
        {"city": "Москва", "phone": "+7-888-888-8888",
            "email": "info@geekshop.ru", "address": "В пределах МКАД"},
        {
            "city": "Екатеринбург",
            "phone": "+7-777-777-7777",
            "email": "info_yekaterinburg@geekshop.ru",
            "address": "Близко к центру",
        },
        {
            "city": "Владивосток",
            "phone": "+7-999-999-9999",
            "email": "info_vladivostok@geekshop.ru",
            "address": "Близко к океану",
        },
    ]
    content = {"title": title, "visit_date": visit_date,
               "locations": locations}
    return render(request, "mainapp/help.html", content)
