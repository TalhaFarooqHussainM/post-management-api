import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search
    content = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search

    class Meta:
        model = Post
        fields = ['title', 'content']