from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.


def home(request):
    template = loader.get_template('views/home.html')
    return HttpResponse(template.render())

def login(request): 
    template = loader.get_template('views/login.html')
    return HttpResponse(template.render())

def slicer(request):
    template = loader.get_template('views/slicer.html')
    return HttpResponse(template.render())