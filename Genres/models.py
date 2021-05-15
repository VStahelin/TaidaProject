from django.db import models


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    mal_id = models.IntegerField(blank=False, unique=True)
    type = models.CharField(blank=False, max_length=10)
    name = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.name