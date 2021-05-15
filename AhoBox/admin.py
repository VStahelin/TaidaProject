from django.contrib import admin

from AhoBox.models import AnimeList


@admin.register(AnimeList)
class AnimeListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_owner', 'name', 'privacy', 'description')
