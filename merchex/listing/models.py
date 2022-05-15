# listings/models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Band(models.Model):  # Model Used for the category Band here you can modify the parameters of the Bands model app
    def __str__(self):
        return f'{self.name}'  # Function return the name field of a band occurrences

    name = models.fields.CharField(max_length=100)  # Parameter name of a Band

    class Genre(models.TextChoices):  # choice list of Band model
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        TECHNO = 'TEC'

    genre = models.fields.CharField(choices=Genre.choices, max_length=5)  # Utilisation of the Band list model
    biography = models.fields.CharField(max_length=1000)  # Parameter for input a biography of the band
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)])
    # Parameter for the year of formation for a band
    active = models.fields.BooleanField(default=True)  # Parameter boolean for show if the group is active or not
    official_homepage = models.fields.URLField(null=True, blank=True)
    # (optional) Parameter for input a URL of a band website


class Notification(models.Model):
    title = models.fields.CharField(max_length=100)  # title of a annonce about a band


class Goodies(models.Model):
    def __str__(self):
        return f'{self.label}'
    label = models.fields.CharField(max_length=100)  # Label of a Goodies
    description = models.fields.CharField(max_length=500)  # Description of a Goodies
    sold = models.fields.BooleanField(default=False)  # Mention sold of a goodies
    year = models.fields.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(2022)])

    # year of creation or production of the goodies

    class Type(models.TextChoices):
        DISQUES = 'disk'
        ENREGISTREMENTS ='RECORDS'
        VETEMENTS = 'CLOTHING'
        AFFICHES = 'POSTERS'
        DIVERS = 'MISCELLANEOUS'

    type = models.fields.CharField(choices=Type.choices, max_length=50)  # Usage of the Type model create upper
