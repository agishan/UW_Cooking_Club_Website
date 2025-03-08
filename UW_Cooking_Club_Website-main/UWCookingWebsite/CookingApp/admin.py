from django.contrib import admin
from .models import Recipe, Cooking_Class

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Cooking_Class)