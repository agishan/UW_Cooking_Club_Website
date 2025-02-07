from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    procedure = models.CharField(max_length=1000)
    cuisine = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    meal_type = models.CharField(max_length=100)
    images = models.ImageField(default='',upload_to='Recipe_Images/')

