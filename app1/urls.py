from django.urls import path
from app1.views import index, catalog, forum

urlpatterns = [
    path('', index),
    path('catalog/', catalog),
    path('forum/', forum),
]