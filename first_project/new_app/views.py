from django.shortcuts import render, redirect

from .models import *
# from django

# Create your views here.

def index(request):
    profile = Profile.objects.all()
    context = {
        'profile':profile
    }
    return render(request, 'new_app/index.html',context) 
def contact(request):
    return render(request, 'new_app/contact.html')
def projects(request):
    return render(request, 'new_app/projects.html')
def resume(request):
    return render(request, 'new_app/resume.html')

