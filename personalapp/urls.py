from django.urls import path
import personalapp.views as personalapp


app_name = 'personalapp'
urlpatterns = [
path('', personalapp.main, name='main'),
path('articles/', personalapp.articles, name='articles'),
path('articles-create/', personalapp.ArticleCreateView.as_view(), name='articles_create'),
path('articles-update/<int:pk>/', personalapp.ArticleUpdateView.as_view(), name='articles_update'),
]
