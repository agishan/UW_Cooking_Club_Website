from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    images = models.ImageField(default='',upload_to='Recipe_Images/')
    cooking_class = models.CharField(max_length=200,default='')
    description = models.TextField(default='')
    difficulty = models.DecimalField(max_digits=2,decimal_places=1,default=0.0)
    prep_time = models.CharField(max_length=200,default='')
    cook_time = models.CharField(max_length=200,default='')
    total_time = models.CharField(max_length=200,default='')
    serving_size = models.DecimalField(max_digits=2,decimal_places=1,default=0.0)
    equipment = models.TextField(default='')
    ingredients = models.TextField(default='')
    procedure = models.TextField(default='')

class Cooking_Class(models.Model):
    images = models.ImageField(default='',upload_to='Cooking_Class_Images/')
    date = models.DateField()
    instructor = models.CharField(max_length=200,default='')
    recipes = models.TextField(default='')



