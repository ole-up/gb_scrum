import random
from functools import reduce

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from authapp.models import CustomUser
from mainapp.filters import ArticleFilter
from mainapp.forms import CommentForm
from mainapp.models import Article, ArticleCategory, Comment


def get_articles(category_id):
    return Article.objects.filter(category_id=category_id).reverse() if category_id else \
        Article.objects.all().reverse()


def get_category_name_by_id(category_id):
    return ArticleCategory.objects.filter(id=category_id).first().name


def articles(request, category_id=None, page=1):
    per_page = 5
    article_filter = search_articles(request)
    paginator = Paginator(get_articles(category_id), per_page)
    try:
        articles_paginator = paginator.page(page)
    except PageNotAnInteger:
        articles_paginator = paginator.page(1)
    except EmptyPage:
        articles_paginator = paginator.page(paginator.num_pages)
    title = {
        'page_title': get_category_name_by_id(category_id) if category_id else "Главная",
        'title_row_1': "Наш Хабр" if category_id else "Добро пожаловать на портал",
        'title_row_2': get_category_name_by_id(category_id) if category_id else "Наш Хабр"
    }
    context = {
        'title': title,
        'articles': articles_paginator,
        'categories': ArticleCategory.objects.all(),
        'author': CustomUser.objects.filter(id=random.randint(1, CustomUser.objects.latest('id').id)).first(),
        'filter': article_filter
    }
    return render(request, 'mainapp/index.html', context)


def view_article(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article=article_id).all()
    form = CommentForm(initial={'author': request.user, 'article_id': article.id})
    article_filter = search_articles(request)
    title = {
        'page_title': article.category,
        'title_row_1': "Наш Хабр",
        'title_row_2': article.category
    }

    content = {'title': title,
               'article': article,
               'categories': ArticleCategory.objects.all(),
               'author': CustomUser.objects.filter(id=article.author.id).first(),
               'comments': comments,
               'form': form,
               'filter': article_filter
               }
    if request.method == 'POST':
        print(request.POST)
        form = CommentForm(data=request.POST, initial={'author': request.user, 'article_id': article.id})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:article', args=[article.id]))

    return render(request, 'mainapp/article.html', content)


def moderate_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.for_moderation = True
    article.save()
    return HttpResponseRedirect(reverse('personal:articles'))


def publish_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.for_moderation = False
    article.is_published = True
    article.save()
    return HttpResponseRedirect(reverse('personal:moderation'))


def refuse_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.for_moderation = False
    article.is_published = False
    article.save()
    return HttpResponseRedirect(reverse('personal:moderation'))


def unpublish_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.for_moderation = False
    article.is_published = False
    article.save()
    return HttpResponseRedirect(reverse('personal:articles'))


def delete_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.is_deleted = True
    article.save()
    return HttpResponseRedirect(reverse('personal:articles'))


def search_articles(request):
    article_filter = None
    result = Article.objects.all()
    query = request.GET.get("query", '').split()
    if query:
        filters = reduce(lambda x, y: x | y, [
            (Q(title__icontains=word) |
             Q(author__first_name__icontains=word) |
             Q(author__last_name__icontains=word) |
             Q(description__icontains=word)
             )
            for word in query
        ])
        result = result.filter(filters).distinct()
        article_filter = ArticleFilter(request.GET, queryset=result)
    return article_filter
