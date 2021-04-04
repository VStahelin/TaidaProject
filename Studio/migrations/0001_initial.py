# Generated by Django 3.1.7 on 2021-04-04 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Genres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mal_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Genres.type')),
            ],
        ),
    ]
