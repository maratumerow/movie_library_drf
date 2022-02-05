from django_filters import rest_framework as filters
from . import models


class MovieFilter(filters.FilterSet):
    """Фильтр фильмов"""

    year = filters.RangeFilter()

    class Meta:
        model = models.Movie
        fields = ['year', 'country', 'genre']
