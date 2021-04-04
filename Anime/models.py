from django.db import models

from Genres.models import Type
from Studio.models import Studio


class Anime(models.Model):
    mal_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    trailer_url = models.URLField()
    titles = models.TextField()  # Dict '{'title': 'Hunter x Hunter (2011)', 'title_english': 'Hunter x Hunter', 'title_japanese': 'HUNTER×HUNTER（ハンター×ハンター）','title_synonyms': ['HxH (2011)']}'
    type = models.CharField(max_length=5)
    score = models.DecimalField(max_digits=3, decimal_places=3)
    scored_by = models.IntegerField()
    rank = models.IntegerField()
    episodes = models.IntegerField()
    broadcast = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING)
    genres = models.CharField(max_length=100)  # List '(1,10,23,44)'
    synopsis = models.TextField()

    def __str__(self):
        return self.name


class Studios(models.Model):
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING)
    anime_mal_id = models.ForeignKey(Anime, on_delete=models.DO_NOTHING)
    studio_mal_id = models.ForeignKey(Studio, on_delete=models.DO_NOTHING)


class AnimeCard(models.Model):
    mal_id = models.IntegerField()
    title = models.CharField(max_length=100)
    synopsis = models.TextField()
    image_url = models.URLField()
