# Generated by Django 3.1.7 on 2021-05-01 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Studio', '0002_auto_20210501_1813'),
        ('Genres', '0002_auto_20210404_0145'),
        ('Anime', '0002_auto_20210404_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='studios',
            field=models.ManyToManyField(to='Studio.Studio'),
        ),
        migrations.RemoveField(
            model_name='anime',
            name='genres',
        ),
        migrations.AddField(
            model_name='anime',
            name='genres',
            field=models.ManyToManyField(to='Genres.Genre'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='type',
            field=models.CharField(max_length=5),
        ),
        migrations.DeleteModel(
            name='Studios',
        ),
    ]
