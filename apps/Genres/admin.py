from django.contrib import admin

from Genres.models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('mal_id', 'name', 'type')
