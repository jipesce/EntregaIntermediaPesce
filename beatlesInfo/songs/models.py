from django.db import models

# Create your models here.

class Songs(models.Model):
  name = models.CharField(max_length=60)
  composer = models.CharField(max_length=60)
  album = models.CharField(max_length=60)
  year = models.IntegerField()

class Instruments(models.Model):
  type = models.CharField(max_length=40)
  brand = models.CharField(max_length=40)
  model = models.CharField(max_length=40)
  year = models.IntegerField()

class Movies(models.Model):
  name = models.CharField(max_length=40)
  year = models.IntegerField()
