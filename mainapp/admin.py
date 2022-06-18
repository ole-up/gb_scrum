from django.contrib import admin

from .models import Article, ArticleCategory

admin.site.register(ArticleCategory)
admin.site.register(Article)
