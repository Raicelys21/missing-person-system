from django.db import models

# Create your models here.
class Gallery(models.Model):
    photo = models.ImageField(upload_to="gallery")
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)

class Identify(models.Model):
    photo = models.ImageField(upload_to="identify")