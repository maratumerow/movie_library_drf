from django.contrib import admin

from . import models


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title',)


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
