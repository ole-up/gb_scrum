from django.shortcuts import render

def main(request):
    title = {
        "page_title": "Личный кабинет",
        "title_row_1": "Наш Хабр",
        "title_row_2": "Личный кабинет"
    }
    content = {"title": title}
    return render(request, "personalapp/personal.html", content)

def profile(request):
    title = {
        "page_title": "Личный кабинет",
        "title_row_1": "Наш Хабр",
        "title_row_2": "Личный кабинет"
    }
    content = {"title": title}
    return render(request, "personalapp/profile.html", content)

def articles(request):
    title = {
        "page_title": "Личный кабинет",
        "title_row_1": "Наш Хабр",
        "title_row_2": "Личный кабинет"
    }
    content = {"title": title}
    return render(request, "personalapp/my_articles.html", content)
