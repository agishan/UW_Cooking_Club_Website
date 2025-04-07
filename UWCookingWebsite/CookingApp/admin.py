from django.contrib import admin
from .models import Recipe, Cooking_Class, Club_Member
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Cooking_Class)
admin.site.register(Club_Member)