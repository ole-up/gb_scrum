from django.urls import path

from mainapp.views import view_article, articles

app_name = 'mainapp'

urlpatterns = [
    path('', articles, name='index'),
    path('<int:category_id>/', articles, name='articles'),
    path('page/<int:page>/', articles, name='page'),
    path('article/<int:article_id>/', view_article, name='article'),
]