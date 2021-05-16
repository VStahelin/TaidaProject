from django.conf import settings
from django.db import models

from Anime.models import Anime


class AnimeCardList(models.Model):
    models.AutoField(primary_key=True)

    class Status(models.TextChoices):
        TO_WATCH = 'TW', ('To watch')
        WATCHING = 'WG', ('Watching')
        WATCHED = 'WD', ('Watched')

    user_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, default=1)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, blank=True)
    status = models.CharField(blank=False, max_length=2, choices=Status.choices, default=Status.TO_WATCH)
    last_episode_watched = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.anime.name


class List(models.Model):
    models.AutoField(primary_key=True)
    user_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, default=1)
    name = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=True, default='No description')
    animes = models.ManyToManyField(AnimeCardList, blank=True)
    type = models.CharField(blank=False, max_length=5, default='')

    def __str__(self):
        return self.name
