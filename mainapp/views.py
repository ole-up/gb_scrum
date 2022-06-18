import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from mainapp.models import Article, ArticleCategory


def get_articles_ordered_by_date(category_id):
    return Article.objects.filter(category_id=category_id).order_by('edit_date').reverse() if category_id else \
        Article.objects.all().order_by('edit_date').reverse()


def get_category_name_by_id(category_id):
    return ArticleCategory.objects.filter(id=category_id).first().name


def articles(request, category_id=None, page=1):
    per_page = 5
    paginator = Paginator(get_articles_ordered_by_date(category_id), per_page)
    try:
        articles_paginator = paginator.page(page)
    except PageNotAnInteger:
        articles_paginator = paginator.page(1)
    except EmptyPage:
        articles_paginator = paginator.page(paginator.num_pages)
    title = {
        "page_title": get_category_name_by_id(category_id) if category_id else "Главная",
        "title_row_1": "Наш Хабр" if category_id else "Добро пожаловать на портал",
        "title_row_2": get_category_name_by_id(category_id) if category_id else "Наш Хабр"
    }
    context = {
        'title': title,
        'articles': articles_paginator,
        'categories': ArticleCategory.objects.all(),
    }
    return render(request, 'mainapp/index.html', context)


def view_article(request, article_id):
    article = Article.objects.get(id=article_id)

    title = {
        "page_title": article.category,
        "title_row_1": "Наш Хабр",
        "title_row_2": article.category
    }

    content = {"title": title,
               "article": article,
               'categories': ArticleCategory.objects.all(),}
    return render(request, "mainapp/article.html", content)
