import django.http.request
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

import backend.art_gen_server.settings
from .models import Image
from .serializers import ImageSerializer

def index(request):
    return django.http.HttpResponse("Hi! This is the index for art_gen_server's api/v0 .")

# def home(request):
#     return render(request, "home.html")

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
# Path: urls.py
def getJeff(request):
    return None


def getJeffBytes(request):
    with open(backend.art_gen_server.settings.MEDIA_ROOT + "/jeff.jpg", "rb") as image:
        return HttpResponse(image.read(), content_type="image/jpeg")

def getJeffUrl(request):
    return None
