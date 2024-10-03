from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Hello world')
def catalog(request):
    return HttpResponse('catalog world')
def forum(request):
    return HttpResponse('forum мир')