from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=200, db_index=True)

class Slide_of_collection(models.Model):
    image = models.ImageField(upload_to='images/lookbook',  blank=True)
    image2 = models.ImageField(upload_to='images/lookbook',  blank=True)
    collection = models.ManyToManyField(Collection)
    description = models.TextField(max_length=300)
    description2 = models.TextField(max_length=300)