from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recipes/", views.recipes, name="recipes"),
    path("recipeAPI/", views.recipeAPI, name="recipeAPI"),
    re_path(r'^media/(?P<path>.*)$', views.get_image),
]