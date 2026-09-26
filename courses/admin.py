from django.contrib import admin
from .models import Courses,Catagory,Tag,Article
# Register your models here.

admin.site.register(Courses)
admin.site.register(Catagory)
admin.site.register(Tag)
admin.site.register(Article)