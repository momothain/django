import os

import django
import django.http
from django.conf import settings
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from backend.art_gen_server.db_models.image import Image
from .serializers import ImageSerializer


def index(request):
    return django.http.HttpResponse("Hi! This is the index for art_gen_server's api/v0 .")


# def home(request):
#     return render(request, "home.html")

class ImageView(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.method == 'POST':
            # Assuming you have a file input in your form with name 'image_file'
            image_file = request.FILES.get('image')
            name = request.POST.get('name', 'default_name')
            
            new_image = Image(name=name, image_file=image_file)
            new_image.save()
            
            return HttpResponse("Image uploaded successfully!")
        else:
            return HttpResponse("Only POST requests are accepted here.")
        
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# Path: urls.py
def get_jeff(request):
    return None


def get_jeff_bytes(request):
    file_path = os.path.join(settings.MEDIA_ROOT, "jeff.jpg")
    with open(file_path, "rb") as image:
        return HttpResponse(image.read(), content_type="image/jpeg")



def get_jeff_url(request):
    return None
