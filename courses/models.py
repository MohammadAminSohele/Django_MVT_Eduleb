from django.db import models

# Create your models here.

class Catagory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    images = models.image
    catagory = models.ManyToManyField(Catagory)
    price = models.IntegerField()
    time = models.TimeField()

    def __str__(self):
        return self.title