from django.http import JsonResponse, Http404, HttpResponseNotModified, FileResponse
from django.conf import settings
from django.db.models import Q
from django.utils._os import safe_join
from django.utils.http import http_date
from django.utils.translation import gettext as _
from django.views.static import was_modified_since
from pathlib import Path
import mimetypes, posixpath

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe, Cooking_Class
from .serializers import RecipeSerializer, EventSerializer

# API to get all recipes
@api_view(['GET'])
def recipe_list(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response({"recipes": serializer.data})

# API to get a single recipe by ID
@api_view(['GET'])
def recipe_detail(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
    except Recipe.DoesNotExist:
        return Response({"error": "Recipe not found"}, status=404)

# API to get all events
@api_view(['GET'])
def event_list(request):
    events = Cooking_Class.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response({"events": serializer.data})

# Serve images
def get_image(request, path=""):
    """
    Retrieve a media file.

    Route: [GET] /cdn/media/:path_to_file
    """
    # Get Path
    filepath = get_filepath(path=path)

    # Fail Directory or Not Found
    if filepath.is_dir() or not filepath.exists():
        raise Http404(_(f"“{filepath}” is not accessible"))

    # Respect the If-Modified-Since header.
    statobj = filepath.stat()
    if not was_modified_since(
        request.META.get("HTTP_IF_MODIFIED_SINCE"), statobj.st_mtime
    ):
        return HttpResponseNotModified()

    # Generate Static View
    content_type, encoding = mimetypes.guess_type(str(filepath))
    content_type = content_type or "application/octet-stream"
    response = FileResponse(filepath.open("rb"), content_type=content_type)
    response.headers["Last-Modified"] = http_date(statobj.st_mtime)
    if encoding:
        response.headers["Content-Encoding"] = encoding
    return response

# Helper function to get the file path
def get_filepath(path: str) -> Path:
    """
    Retrieves the path object of a static file.

    Args:
        path: Filepath of file within MEDIA_ROOT.

    Returns:
        A Filepath object of the file.
    """
    path = posixpath.normpath(path).lstrip("/")
    return Path(safe_join(settings.MEDIA_ROOT, path))
