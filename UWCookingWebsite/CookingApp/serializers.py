from rest_framework import serializers
from .models import Recipe, Cooking_Class

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooking_Class
        fields = '__all__'
