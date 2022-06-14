from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from mainapp.models import Habr
from personalapp.forms import ArticleForm


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


class ArticleCreateView(CreateView):
    model = Habr
    template_name = 'personalapp/create_article.html'
    form_class = ArticleForm
    success_url = reverse_lazy('personal:articles')

    def get_context_data(self, **kwargs):
        context = super(ArticleCreateView, self).get_context_data(**kwargs)
        context['title'] = {
            "page_title": "Личный кабинет",
            "title_row_1": "Наш Хабр",
            "title_row_2": "Личный кабинет"
        }
        return context

    def dispatch(self, request, *args, **kwargs):
        return super(ArticleCreateView, self).dispatch(request, *args, **kwargs)
