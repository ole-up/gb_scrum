import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView
from django.views.generic.edit import BaseCreateView

from mainapp.models import Article, ArticleCategory, Comment
from mainapp.forms import CommentForm
from authapp.models import CustomUser


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
        'page_title': get_category_name_by_id(category_id) if category_id else "Главная",
        'title_row_1': "Наш Хабр" if category_id else "Добро пожаловать на портал",
        'title_row_2': get_category_name_by_id(category_id) if category_id else "Наш Хабр"
    }
    context = {
        'title': title,
        'articles': articles_paginator,
        'categories': ArticleCategory.objects.all(),
        'author': CustomUser.objects.filter(id=random.randint(1, CustomUser.objects.latest('id').id)).first(),
    }
    return render(request, 'mainapp/index.html', context)


def view_article(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article=article_id).all()
    form = CommentForm(initial={'author': request.user, 'article_id': article.id})
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
