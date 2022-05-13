# listings/models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Band(models.Model):
    name = models.fields.CharField(max_length=100)

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)


class Notification(models.Model):
    title = models.fields.CharField(max_length=100)


class Goodies(models.Model):
    label = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=500)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(2022)])

    class Type (models.TextChoices):
        RECORDS = 'Disques/Enregistrements'
        CLOTHING = 'Vêtements'
        POSTERS = 'Affiches'
        MISCELLANEOUS = 'Divers'

    type = models.fields.CharField(choices=Type.choices, max_length=50)
