from django.contrib import admin

from . import models


class MovieShotsInline(admin.TabularInline):
    model = models.MovieShots
    extra = 3


class MovieCommentsInline(admin.TabularInline):
    model = models.Comment
    extra = 1


class MovieLikesInline(admin.TabularInline):
    model = models.MovieLike
    extra = 1


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [MovieShotsInline, MovieCommentsInline, MovieLikesInline]


@admin.register(models.MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(models.Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(models.Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(models.Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country',)


@admin.register(models.Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ('language',)


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'text', 'parent')


@admin.register(models.MovieLike)
class MovieLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie')
