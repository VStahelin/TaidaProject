from django.db import models

from Genres.models import Type


class Studio(models.Model):
    mal_id = models.IntegerField()
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
