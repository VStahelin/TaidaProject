from django.contrib import admin

from Studio.models import Studio


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ('mal_id', 'name')
