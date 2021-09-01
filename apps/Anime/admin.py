from django.contrib import admin

from Anime.models import Anime, AnimeCard


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'mal_id', 'name', 'type')


@admin.register(AnimeCard)
class AnimeCardAdmin(admin.ModelAdmin):
    list_display = ('mal_id', 'title', 'synopsis')
