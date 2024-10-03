from django.urls import path
from app2.views import index, scp, contact

urlpatterns = [
    path('', index),
    path('scp/', scp),
    path('contact/', contact),
]