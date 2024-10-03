from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Третье приложение))')
def second(request):
    return HttpResponse('Второй пункт')
def third(request):
    return HttpResponse('Книга')