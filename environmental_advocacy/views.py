from django.shortcuts import render
from .models import EnvironmentalProject

def project_list(request):
    projects = EnvironmentalProject.objects.all()
    return render(request, 'environmental_advocacy/project_list.html', {'projects': projects})

def home(request):
    return render(request, 'home.html')