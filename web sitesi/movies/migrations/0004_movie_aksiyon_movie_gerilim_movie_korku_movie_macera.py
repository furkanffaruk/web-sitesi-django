# Generated by Django 4.2.1 on 2023-05-23 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_main_alter_movie_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='aksiyon',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='gerilim',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='korku',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='macera',
            field=models.BooleanField(default=False),
        ),
    ]
