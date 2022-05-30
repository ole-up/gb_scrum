import datetime

from django.shortcuts import render


def main(request):
    title = "главная"
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
    title = "Новости"
    links_menu = [
        {"href": "habr_all", "name": "Все"},
        {"href": "habr_home", "name": "ИТ"},
        {"href": "habr_office", "name": "Языки программирования"},
        {"href": "habr_modern", "name": "Микроконтроллеры"},
        {"href": "habr_classic", "name": "Хакерам"},
    ]
    same_habr = [
        {"name": "Отличная новость", "desc": "Не оторваться.",
            "image_src": "", "alt": "..."},
        {"name": "Свежая новость", "desc": "То-то еще будет",
            "image_src": "", "alt": "..."},
        {
            "name": "Новости для хакинга",
            "desc": "Просто попробуйте.",
            "image_src": "",
            "alt": "...",
        },
    ]
    content = {"title": title, "links_menu": links_menu,
               "same_habr": same_habr}
    return render(request, "mainapp/habr.html", content)


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
    content = {"title": title, "visit_date": visit_date,
               "locations": locations}
    return render(request, "mainapp/help.html", content)
