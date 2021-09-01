from django.contrib import admin

from Lists.models import AnimeCardList, List


@admin.register(AnimeCardList)
class AnimeCardListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_owner', 'anime', 'status', 'last_episode_watched')


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_owner', 'name', 'description')
