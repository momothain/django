from django.db import models
from django.core.validators import FileExtensionValidator


class ImageLayer(models.Model):
    name = models.CharField(max_length=255)
    pixel_data = models.TextField(help_text="JSON-encoded pixel data")
    pixel_data_file = models.FileField(upload_to='image_layers/', validators=[FileExtensionValidator(['json'])])

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=255)
    layers = models.ManyToManyField(ImageLayer, related_name='images')

    def __str__(self):
        return self.title
