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

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Image
from .serializers import ImageSerializer

class ImageView(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


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
