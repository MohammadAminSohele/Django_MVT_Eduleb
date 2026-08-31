from django.shortcuts import render
from .models import Course
# Create your views here.

def home_page(request):
    context={
        'Courses':Course.objects.all()
    }
    return render(request,'home_page.html',context)