from rest_framework import serializers
from django.contrib.auth.models import User

from . import models


class FilterCommentListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children комментариев"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователей"""

    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializer(serializers.ModelSerializer):
    """Сериализация комментариев"""

    children = RecursiveSerializer(many=True)
    user = UserSerializer()

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = models.Comment
        exclude = ('lft', 'rght', 'tree_id', 'level')


class GenreSerializer(serializers.ModelSerializer):
    """Сериализация жанров"""

    class Meta:
        model = models.Genre
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    """Сериализация режисеров"""

    class Meta:
        model = models.Director
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    """Сериализация актеров"""

    class Meta:
        model = models.Actor
        fields = '__all__'


class WriterSerializer(serializers.ModelSerializer):
    """Сериализация сценаристов"""

    class Meta:
        model = models.Writer
        fields = '__all__'


class ProducerSerializer(serializers.ModelSerializer):
    """Сериализация продюсеров"""

    class Meta:
        model = models.Producer
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    """Сериализация страны"""

    class Meta:
        model = models.Country
        fields = '__all__'


class TranslationSerializer(serializers.ModelSerializer):
    """Сериализация перевода, озвучки"""

    class Meta:
        model = models.Translation
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    """Сериализация фильмов"""

    comment = CommentSerializer(many=True, read_only=True)
    genre = GenreSerializer(many=True)
    director = DirectorSerializer(many=True)
    actor = ActorSerializer(many=True)
    writer = WriterSerializer(many=True)
    producer = ProducerSerializer(many=True)
    country = CountrySerializer(many=True)
    translation = TranslationSerializer(many=True)
    count_like = serializers.SerializerMethodField()

    def get_count_like(self, obj):
        return obj.likes.count()

    class Meta:
        model = models.Movie
        fields = '__all__'


class CreateCommentSerializer(serializers.ModelSerializer):
    """Добавление комментариев к фильму"""

    class Meta:
        model = models.Comment
        fields = ('id', 'movie', 'text', 'parent')


class LikeSerializer(serializers.ModelSerializer):
    """Сериализация лайков к фильму"""

    user = UserSerializer(read_only=True)

    class Meta:
        model = models.MovieLike
        fields = ('user', 'movie')
