# Generated by Django 3.1.7 on 2021-05-01 21:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Studio', '0002_auto_20210501_1813'),
        ('Anime', '0003_auto_20210501_1813'),
        ('Genres', '0002_auto_20210404_0145'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Type',
        ),
        migrations.AddField(
            model_name='genre',
            name='type',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='genre',
            name='mal_id',
            field=models.IntegerField(),
        ),
    ]
