from django.conf import settings
from django.db import models

from Anime.models import Anime


class AnimeList(models.Model):
    user_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=200)
    privacy = models.BooleanField(default=True, help_text='True = Public, False = Private ')
    animes = models.ManyToManyField(Anime)
    description = models.TextField(default='')

    # subscribers = models.ManyToManyField(User.get_username(), default=True)

    def __str__(self):
        return self.name
