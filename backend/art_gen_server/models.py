from django.db import models

# Create your models here.c
class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')  # 'images/' is the directory where uploaded images will be stored
    uploaded_at = models.DateTimeField(auto_now_add=True)
