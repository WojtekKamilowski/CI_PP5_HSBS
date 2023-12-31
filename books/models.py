from django.db import models
from django.db.models import IntegerField, Model
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator


# Customised model for books offered by the store


class Era(models.Model):
    name = models.CharField(max_length=260)
    friendly_name = models.CharField(max_length=260, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Book(models.Model):
    era = models.ForeignKey(
        'Era', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=260, null=True,
                           blank=False, unique=True)
    name = models.CharField(max_length=260, null=True, blank=False)
    author = models.CharField(max_length=260)
    published = models.DateField(null=True, blank=False)
    pages = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(1)
    ])
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[
        MinValueValidator(1)
    ])
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ])
    image_url = models.URLField(max_length=1030, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
