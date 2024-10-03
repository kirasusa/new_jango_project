from django.urls import path
from app3.views import index, second, third

urlpatterns = [
    path('', index),
    path('second/', second),
    path('third/', third),
]