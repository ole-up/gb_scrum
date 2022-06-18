from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from mainapp.models import Article, ArticleCategory
from personalapp.forms import ArticleForm


def main(request):
    title = {
        "page_title": "Личный кабинет",
        "title_row_1": "Наш Хабр",
        "title_row_2": "Личный кабинет"
    }
    content = {"title": title,
               'categories': ArticleCategory.objects.all()}
    return render(request, "personalapp/personal.html", content)


def articles(request):
    user_articles = Article.objects.filter(author=request.user)
    title = {
        "page_title": "Личный кабинет",
        "title_row_1": "Наш Хабр",
        "title_row_2": "Личный кабинет"
    }
    content = {"title": title,
               'articles': user_articles,
               'categories': ArticleCategory.objects.all()}
    return render(request, "personalapp/my_articles.html", content)


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'personalapp/create_article.html'
    form_class = ArticleForm
    success_url = reverse_lazy('personal:articles')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ArticleCreateView, self).get_context_data(**kwargs)
        context['title'] = {
            "page_title": "Личный кабинет",
            "title_row_1": "Наш Хабр",
            "title_row_2": "Личный кабинет"
        }
        context['categories'] = ArticleCategory.objects.all()
        return context

    def dispatch(self, request, *args, **kwargs):
        return super(ArticleCreateView, self).dispatch(request, *args, **kwargs)


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'personalapp/edit_article.html'
    form_class = ArticleForm
    success_url = reverse_lazy('personal:articles')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ArticleUpdateView, self).get_context_data(**kwargs)
        context['title'] = {
            "page_title": "Личный кабинет",
            "title_row_1": "Наш Хабр",
            "title_row_2": "Личный кабинет"
        }
        context['categories'] = ArticleCategory.objects.all()
        return context

    def dispatch(self, request, *args, **kwargs):
        return super(ArticleUpdateView, self).dispatch(request, *args, **kwargs)
