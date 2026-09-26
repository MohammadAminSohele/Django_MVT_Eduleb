from django.db import models
import os 
from accounts.models import User
# Create your models here.


def get_file_name_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    name,ext = get_file_name_ext(filename)
    final_name = f'{instance.id}-{instance.title}{ext}'
    return f'courses/{final_name}'

def upload_image_path_course(instance,filename):
    name,ext = get_file_name_ext(filename)
    final_name = f'{instance.id}-{instance.title}{ext}'
    return f'course/{final_name}'

def upload_image_path_catagory(instance,filename):
    name,ext = get_file_name_ext(filename)
    final_name = f'{instance.id}-{instance.title}{ext}'
    return f'catagory/{final_name}'

def upload_image_path_article(instance,filename):
    name,ext = get_file_name_ext(filename)
    final_name = f'{instance.id}-{instance.title}{ext}'
    return f'article/{final_name}'      

class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    status = models.BooleanField(default=True)
    tag = models.ManyToManyField(Tag)
    description = models.TextField()
    images = models.ImageField(upload_to=upload_image_path_article)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Catagory(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)
    images = models.ImageField(upload_to=upload_image_path_catagory)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Courses(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    instructor = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    catagory = models.ManyToManyField(Catagory,related_name='courses')
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to=upload_image_path_course)
    price = models.DecimalField(max_digits=10,decimal_places=0)
    description = models.TextField()
    time = models.CharField(max_length=50,help_text='3 Hrs 30 Min')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    discout_price = models.DecimalField(max_digits=10,decimal_places=0,blank=True,null=True)

    def __str__(self):
        return self.title