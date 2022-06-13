from django.urls import path
import personalapp.views as personalapp
app_name = 'personalapp'
urlpatterns = [
path('', personalapp.main, name='main'),
path('profile/', personalapp.profile, name='profile'),
path('articles/', personalapp.articles, name='articles'),
]