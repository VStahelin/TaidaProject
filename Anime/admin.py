from django.contrib import admin

from Anime.models import Anime, Studios


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'mal_id', 'name', 'type')


@admin.register(Studios)
class StudiosAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'anime_mal_id', 'studio_mal_id')
