from django.conf import settings
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Movie(models.Model):
    """Фильм"""

    title = models.CharField('Название', max_length=128)
    description = models.TextField('Описание')
    date_add = models.DateTimeField('Дата добавления', auto_now_add=True)
    date_update = models.DateTimeField('Дата обновления', auto_now=True)
    poster = models.ImageField('Постер', upload_to='movie/poster/', blank=True)
    director = models.ManyToManyField('Director', verbose_name='Режисер')
    actor = models.ManyToManyField('Actor', verbose_name='Актер')
    writer = models.ManyToManyField('Writer', verbose_name='Сценарист')
    producer = models.ManyToManyField('Producer', verbose_name='Продюсер')
    genre = models.ManyToManyField('Genre', verbose_name='Жанр', blank=True)
    world_premiere = models.DateField('Премьера в мире', blank=True)
    russia_premiere = models.DateField('Премьера в России', blank=True)
    country = models.ManyToManyField('Country', verbose_name='Страна')
    year = models.PositiveIntegerField('Год')
    move_time = models.PositiveIntegerField('Длительность', blank=True)
    translation = models.ManyToManyField('Translation', verbose_name='Перевод')
    file_movie = models.FileField('Видео файл', upload_to='movie/movie_file/')
    trailer = models.FileField('Трейлер', upload_to='movie/trailer/')

    def __str__(self):
        return f'{self.title} {self.year}'

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class MovieShots(models.Model):
    """Кадр из фильма"""

    movie = models.ForeignKey(
        'Movie', on_delete=models.CASCADE, related_name='movie_shots'
    )
    title = models.CharField('Заголовок', max_length=128)
    image = models.ImageField(
        'Кадр к фильму',
        upload_to='movie/movie_shots/',
        blank=True,
        help_text='Кадры из фильма',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр'
        verbose_name_plural = 'Кадры'


class MovieLike(models.Model):
    """Лайки к фильму"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    movie = models.ForeignKey(
        'Movie', related_name='likes', on_delete=models.CASCADE)


class Director(models.Model):
    """Режесер фильма"""

    first_name = models.CharField('Имя', max_length=64)
    last_name = models.CharField('Фамилия', max_length=64)
    image = models.ImageField(
        'Фото', upload_to='movie/director/',
        blank=True,
        help_text='Режесер фильма',
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Режесер'
        verbose_name_plural = 'Режесеры'


class Writer(models.Model):
    """Сценарист"""

    first_name = models.CharField('Имя', max_length=64)
    last_name = models.CharField('Фамилия', max_length=64)
    image = models.ImageField(
        'Фото',
        upload_to='movie/writer/',
        blank=True,
        help_text='Сценарист фильма',
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Сценарист'
        verbose_name_plural = 'Сценаристы'


class Producer(models.Model):
    """Продюсер фильма"""

    first_name = models.CharField('Имя', max_length=64)
    last_name = models.CharField('Фамилия', max_length=64)
    image = models.ImageField(
        'Фото',
        upload_to='movie/producer/',
        blank=True,
        help_text='Продюсер фильма',
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Продюсер'
        verbose_name_plural = 'Продюсеры'


class Actor(models.Model):
    """Актер фильма"""

    first_name = models.CharField('Имя', max_length=64)
    last_name = models.CharField('Фамилия', max_length=64)
    image = models.ImageField(
        'Фото', upload_to='movie/actor/', blank=True, help_text='Актер фильма',
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'


class Genre(models.Model):
    """Жанр фильма"""

    title = models.CharField('Жанр', max_length=32, help_text='Жанр фильма')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Country(models.Model):
    """Страна производства фильма"""

    country = models.CharField(
        'Страна', max_length=32, help_text='Страна производства фильма'
    )

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Translation(models.Model):
    """Перевод, озвучка фильма"""

    language = models.CharField(
        'Язык', max_length=32, help_text='Перевод, озвучка фильма'
    )

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = 'Перевод, озвучка'
        verbose_name_plural = 'Переводы, озвучки'


class Comment(MPTTModel):
    """Модель коментариев к фильму"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь'
    )
    movie = models.ForeignKey(
        'Movie', related_name='comment', on_delete=models.CASCADE, verbose_name='Фильм'
    )
    text = models.TextField('Текст комментария')
    date_add = models.DateTimeField('Дата добавления', auto_now_add=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Ответ на комментарий'
    )

    def __str__(self):
        return f'{self.user} - {self.movie} - {self.text}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
