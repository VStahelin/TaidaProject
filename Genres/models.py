from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)
    mal_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    TYPES = (
        ('Manga', 'Manga'),
        ('Anime', 'Anime'),
    )
    type_name = models.CharField(max_length=5, choices=TYPES)

    def __str__(self):
        return self.type_name
