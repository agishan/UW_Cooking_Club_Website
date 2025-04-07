from django.db import models

# Create your models here.

class Cooking_Class(models.Model):
    name = models.CharField(max_length=200,default='unnamed class')
    images = models.ImageField(default='',upload_to='class_images')
    date = models.DateField()
    instructor = models.CharField(max_length=200,default='')

    def __str__(self):
        return self.name
    
    def get_recipes(self):
        return self.recipes.all()

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    images = models.ImageField(default='',upload_to='recipe_images')
    cooking_class_new = models.ForeignKey(
        Cooking_Class,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='recipes')

    description = models.TextField(default='')
    difficulty = models.DecimalField(max_digits=2,decimal_places=1,default=0.0)
    prep_time = models.CharField(max_length=200,default='')
    cook_time = models.CharField(max_length=200,default='')
    total_time = models.CharField(max_length=200,default='')

    serving_size = models.DecimalField(max_digits=2,decimal_places=1,default=0.0)
    equipment = models.TextField(default='')
    ingredients = models.TextField(default='')
    procedure = models.TextField(default='')

    def __str__(self):
        return self.name

class Club_Member(models.Model):
    TEAM_CHOICES = [
        ("ADMIN", "Admin"),
        ("EVENTS", "Events"),
        ("CONTENT", "Content"),
    ]
        
    name = models.CharField(max_length=200)
    team = models.CharField(max_length=200, choices=TEAM_CHOICES,default='ADMIN')
    role = models.CharField(max_length=200)
    images = models.ImageField(default='',upload_to='club_member_images')

    def __str__(self):
        return self.name


