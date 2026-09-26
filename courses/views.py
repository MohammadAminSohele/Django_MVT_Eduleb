from django.shortcuts import render
from .models import Courses,Catagory,Article
# Create your views here.

def home_page(request):
    context={
        'Courses':Courses.objects.all(),
        'Catagory':Catagory.objects.all(),
        'Article':Article.objects.all(),
    }
    return render(request,'home_page.html',context)