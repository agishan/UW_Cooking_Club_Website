from rest_framework import serializers
from .models import Recipe, Cooking_Class, Club_Member

class EventMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooking_Class
        fields = ['id','name']

class RecipeSerializer(serializers.ModelSerializer):
    cooking_class_new = EventMiniSerializer()

    class Meta:
        model = Recipe
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True,read_only=True)

    class Meta:
        model = Cooking_Class
        fields = '__all__'

class ClubMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club_Member
        fields = '__all__'
