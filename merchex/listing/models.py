# listings/models.py
from django.db import models


# Create your models here.


class Band(models.Model):
    name = models.fields.CharField(max_length=100)


class Notification(models.Model):
    title = models.fields.CharField(max_length=100)


class Disc(models.Model):
    label = models.fields.CharField(max_length=50)
    state = models.fields.CharField(max_length=50)
