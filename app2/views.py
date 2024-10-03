from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('hie')
def scp(request):
    return HttpResponse('11')
def contact(request):
    return HttpResponse('privet')