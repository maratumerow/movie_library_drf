from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from . import service
from . import models
from . import serializers
from . import permissions


class MovieViewSet(viewsets.ModelViewSet):
    """Вывод фильмов и фильма"""

    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_class = service.MovieFilter
    search_fields = ('title', 'year', 'genre__title', 'country__country')


class CommentsView(viewsets.ModelViewSet):
    """CRUD комментариев к записи"""

    queryset = models.Comment.objects.all()
    serializer_class = serializers.CreateCommentSerializer
    permission_classes = [IsAuthenticated, permissions.IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeView(viewsets.ModelViewSet):
    """Добавление/Удаление лайка к фильму"""

    queryset = models.MovieLike.objects.all()
    serializer_class = serializers.LikeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
