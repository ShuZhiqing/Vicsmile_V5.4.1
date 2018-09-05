from django.urls import path
from . import views


urlpatterns = [
    path(r'diet', views.diet, name='diet'),
]