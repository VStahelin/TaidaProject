from django.db import models
from django.utils import timezone

from Genres.models import Genre
from Studio.models import Studio


class Anime(models.Model):
    class Type(models.TextChoices):
        MANGA = 'MG', ('Manga')
        ANIME = 'AN', ('Anime')

    models.AutoField(primary_key=True)
    mal_id = models.IntegerField(blank=False, unique=True)
    name = models.CharField(blank=False, max_length=100)
    image_url = models.URLField(blank=True)
    trailer_url = models.URLField(blank=True, default="https://www.youtube.com/watch?v=0vRJPLNF5Cs")
    titles = models.TextField(blank=True,
                              help_text="{'title': 'Hunter x Hunter (2011)', 'title_english': 'Hunter x Hunter', "
                                        "'title_japanese': 'HUNTER×HUNTER（ハンター×ハンター）','title_synonyms': "
                                        "['HxH (2011)']}")

    type = models.CharField(blank=False, max_length=2, choices=Type.choices, default=Type.ANIME)
    score = models.CharField(blank=True, max_length=5, default=0.0)
    scored_by = models.IntegerField(blank=True, default=0)
    rank = models.IntegerField(blank=True, default=99999999)
    episodes = models.IntegerField(blank=False, default=0)
    publication_status = models.CharField(blank=True, max_length=255, default='')
    broadcast = models.CharField(blank=True, max_length=100, default='')
    genres = models.ManyToManyField(Genre, blank=True)
    synopsis = models.TextField(blank=True, default='')
    studios = models.ManyToManyField(Studio, blank=True)
    last_update = models.DateField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name


class AnimeCard(models.Model):
    mal_id = models.IntegerField()
    title = models.CharField(max_length=100)
    synopsis = models.TextField()
    image_url = models.URLField()
