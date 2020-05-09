# Generated by Django 3.0.5 on 2020-05-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_movie_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='banner',
            field=models.ImageField(upload_to='static/media/movies_banner'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='static/media/movies'),
        ),
    ]
