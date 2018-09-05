from django.urls import path
from . import views


urlpatterns = [
    path(r'healthcare', views.healthcare, name='healthcare'),
    path(r'system', views.system, name='system'),
    path(r'cost', views.cost, name='cost'),
    path(r'waiting', views.waiting, name='waiting'),
    path(r'translation', views.translation, name='translation'),
]