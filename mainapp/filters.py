from django.db.models import Q
from django_filters import FilterSet, CharFilter

from mainapp.models import Article


class ArticleFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains')
    first_name = CharFilter(lookup_expr='icontains')
    last_name = CharFilter(lookup_expr='icontains')
    full_name = CharFilter(method='full_name_filter')
    description = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ['title', 'first_name', 'last_name', 'full_name', 'description']

    def full_name_filter(self, queryset, name, value):
        first_name, last_name = value.split()
        return queryset.filter(Q(author__first_name_icontains=first_name) | Q(author__last_name__icontains=last_name))
