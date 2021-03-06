# Generated by Django 3.0.3 on 2020-04-16 06:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='movies')),
                ('category', models.CharField(choices=[('action', 'ACTION'), ('drama', 'DRAMA'), ('comedy', 'COMEDY'), ('romance', 'ROMANCE')], max_length=10)),
                ('language', models.CharField(choices=[('english', 'ENGLISH'), ('german', 'GERMAN')], max_length=10)),
                ('status', models.CharField(choices=[('RA', 'RECENTLY ADDED'), ('MW', 'MOST WATCHED'), ('TR', 'TOP RATED')], max_length=2)),
                ('cast', models.CharField(max_length=100)),
                ('year_of_production', models.DateField()),
                ('views_count', models.IntegerField(default=0)),
                ('movie_trailer', models.URLField(max_length=500)),
                ('created', models.DateTimeField(default=datetime.datetime(2020, 4, 16, 6, 8, 26, 895105, tzinfo=utc))),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('D', 'DOWNLOAD LINK'), ('W', 'WATCH LINK')], max_length=1)),
                ('link', models.URLField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_watch_link', to='movie.Movie')),
            ],
            options={
                'verbose_name_plural': 'Movie Links',
                'db_table': 'db_movielinks',
            },
        ),
    ]
