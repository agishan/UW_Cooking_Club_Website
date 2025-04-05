from django.http import JsonResponse
from django.urls import path
from .views import recipe_list, recipe_detail, event_list, event_detail, club_member_list, club_member_detail, get_image

def api_home(request):
    return JsonResponse({"message": "Welcome to the Cooking Club API!", "routes": [
        "/api/recipes/",
        "/api/recipes/<id>/",
        "/cdn/media/<path>/"
    ]})

urlpatterns = [
    path("", api_home, name="api-home"),  # Default homepage
    path("api/recipes/", recipe_list, name="recipe-list"),
    path("api/recipes/<int:recipe_id>/", recipe_detail, name="recipe-detail"),
    path("api/events/", event_list, name="event-list"),
    path("api/events/<int:event_id>/", event_detail, name="event-detail"),
    path("api/club-members/", club_member_list, name="club-member-list"),
    path("api/club-members/<int:club_member_id>/", club_member_detail, name="club-member-detail"),
    path("cdn/media/<path:path>/", get_image, name="get-image"),
]
