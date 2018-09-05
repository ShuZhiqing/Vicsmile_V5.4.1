from django.shortcuts import render, HttpResponse
from .models import Clinics
from django.db.models import Q
import json


# Create your views here.
# def result(request):
#     return render(request, 'clinic/result.html', context={})


def clinic(request):
    return render(request, 'clinic/clinic.html', context={})


def map(request):
    return render(request, 'clinic/map.html', context={})

# The main search function.
# Users can search clinics by the combination of postcode/region and language .


def search(request):
    # retrieve the clinic info from the database
    queryset_list = Clinics.objects.all()
    # define the template for the result page
    template = 'clinic/result.html'
    # initialize the error message attribute
    error_msg = ''

    mapbox_access_token = 'pk.my_mapbox_access_token'

    # if the method of request is "GET"
    if request.method == 'GET':

        # get destination info from the input form
        destination = request.GET.get('destination', '')
        # get language info from the input form
        language = request.GET.get('language', '')

        # keep the clinics info which are satisfied the conditions
        # filter the clinics by region/postcode and language
        queryset_list = queryset_list.filter(
            Q(electorate__icontains=destination.lower()) |
            Q(postcode__icontains=destination.lower())).filter(Q(language__icontains=language.lower()))
    # if there are no match, return the message
    if not queryset_list:

            error_msg = 'No results.'

    # return the result page
    return HttpResponse(render(request, template, {
        'error_msg':error_msg,
        'queryset_list': queryset_list,
        'mapbox_access_token': mapbox_access_token,
    }))
