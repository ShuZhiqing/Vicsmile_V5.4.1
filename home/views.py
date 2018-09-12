# from django.shortcuts import render
#
#
# # Create your views here.
# def home(request):
#     return render(request, 'home/home.html', context={})
#
from django.shortcuts import render
from clinic.models import Postcode
from healthcare.urls import *

# Create your views here.
# def home(request):
#     return render(request, 'home/home.html', context={})


def home(request):

    template_name = 'home/home.html'

    location_list = Postcode.objects.all()

    queryset = {
        'address': location_list
    }

    return render(request, template_name, queryset)


def password(request):
    return render(request, 'home/password.html', context={})