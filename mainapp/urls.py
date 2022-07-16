from django.urls import path

from mainapp.views import (view_article, articles, moderate_article, publish_article, unpublish_article, delete_article,
                           refuse_article)

app_name = 'mainapp'

urlpatterns = [
    path('', articles, name='index'),
    path('<int:category_id>/', articles, name='articles'),
    path('page/<int:page>/', articles, name='page'),
    path('article/<int:article_id>/', view_article, name='article'),
    path('article-moderate/<int:article_id>/', moderate_article, name='moderate_article'),
    path('article-publish/<int:article_id>/', publish_article, name='publish_article'),
    path('article-refuse/<int:article_id>/', refuse_article, name='refuse_article'),
    path('article-unpublish/<int:article_id>/', unpublish_article, name='unpublish_article'),
    path('article-delete/<int:article_id>/', delete_article, name='delete_article'),
]
