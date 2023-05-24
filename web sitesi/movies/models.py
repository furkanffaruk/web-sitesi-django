from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    release = models.CharField(max_length=150)
    image = models.CharField(max_length=150)
    main = models.BooleanField(default=False)
    macera = models.BooleanField(default=False)
    aksiyon = models.BooleanField(default=False)
    korku = models.BooleanField(default=False)
    gerilim = models.BooleanField(default=False)
    dram = models.BooleanField(default=False)
