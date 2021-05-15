from django.db import models


class Studio(models.Model):
    models.AutoField(primary_key=True)
    mal_id = models.IntegerField(blank=False)
    type = models.CharField(blank=False, max_length=10)
    name = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.name
