# Generated by Django 4.2 on 2023-05-23 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('release', models.CharField(max_length=150)),
                ('image', models.CharField(max_length=150)),
            ],
        ),
    ]
