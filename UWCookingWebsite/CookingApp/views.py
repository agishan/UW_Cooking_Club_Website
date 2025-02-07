from django.shortcuts import render, HttpResponse
from . models import Recipe

# Create your views here.
def home(request):
    return render(request,"home.html")

def recipes(request):
    recipeInfo = Recipe.objects.all()
    return render(request, "recipes.html", {"recipes": recipeInfo})