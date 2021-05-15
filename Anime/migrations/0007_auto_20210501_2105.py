# Generated by Django 3.2 on 2021-05-02 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Anime', '0006_auto_20210501_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='broadcast',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='anime',
            name='publication_status',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='anime',
            name='rank',
            field=models.IntegerField(blank=True, default=99999999),
        ),
        migrations.AlterField(
            model_name='anime',
            name='score',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='anime',
            name='scored_by',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='anime',
            name='synopsis',
            field=models.TextField(blank=True, default=''),
        ),
    ]
