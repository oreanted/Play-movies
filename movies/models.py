from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    movie_rate = models.FloatField()
    movie_quality = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)


class Payment(models.Model):
    costumer_name = models.CharField(max_length=125)
    email = models.EmailField(max_length=125)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    card_holder = models.CharField(max_length=100)
    card_number = models.IntegerField()
    Exp_month = models.CharField(max_length=25)
    Exp_year = models.IntegerField()
    CVV = models.IntegerField()
    cash = models.IntegerField(default=1)

    def __str__(self):
        return self.card_holder
