from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from . models import Recipe
from pathlib import Path
import mimetypes, posixpath
from pathlib import Path

from typing import Type, TypeVar, Union

from django.conf import settings
from django.db.models import Model, Q
from django.utils._os import safe_join
from django.views.static import was_modified_since
from django.http import FileResponse, Http404, HttpResponseNotModified
from django.utils.http import http_date
from django.utils.translation import gettext as _
from django.views import View
from django.views.static import was_modified_since


# Create your views here.
def home(request):
    return render(request,"home.html")

def recipes(request):
    recipeInfo = Recipe.objects.all()
    return render(request, "recipes.html", {"recipes": recipeInfo})

def recipeAPI(request):
    response = Recipe.objects.all().values()
    return JsonResponse({"recipes": list(response)})

def get_image(request, path=""):
    '''
    Retrieve a media file

    # Template from Django serve function #

    Route: [GET] /cdn/media/:path_to_file
    '''
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

def get_filepath(path : str) -> Path:
    """
    Retrieves the path object of a static file

    Args:
        path: Filepath of file within MEDIA_ROOT

    Returns:
        A Filepath object of the file
    """
    path = posixpath.normpath(path).lstrip("/")
    return Path(safe_join(settings.MEDIA_ROOT, path))