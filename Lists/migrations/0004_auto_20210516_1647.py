# Generated by Django 3.2 on 2021-05-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lists', '0003_alter_list_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='animecardlist',
            name='image_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='animecardlist',
            name='studio',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
