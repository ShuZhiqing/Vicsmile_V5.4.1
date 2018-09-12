from django.shortcuts import render, HttpResponse
from .models import Clinics, Postcode
from django.db.models import Q
import re
from math import sin, cos, sqrt, atan2, radians


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
    clinic_list = Clinics.objects.all()
    location_list = Postcode.objects.all()

    # define the template for the result page
    template = 'clinic/result.html'
    # initialize the error message attribute
    error_msg = ''

    # if the method of request is "GET"
    if request.method == 'GET':
        # get destination info from the input form
        # destination = request.GET.get('destination', '')
        # get language info from the input form
        language = request.GET.get('language1', '')

        language2 = request.GET.get('language2', '')

        range = request.GET.get('distance', '')

        group = request.GET.get('group', '')

        curlocation = request.GET.get('destination')

        curlocation = location_list.filter(address__icontains=curlocation)

        tem = []
        queryset_list = []

        for coordinate in curlocation:
            tem.append(coordinate)
            break

        if tem:

            for clinic in clinic_list:
                distance = calculateDistance(tem[0], clinic)
                if distance < float(range):
                    if language in clinic.language and language2 in clinic.language and group in clinic.group:
                        queryset_list.append(clinic)

        # keep the clinics info which are satisfied the conditions
        # filter the clinics by region/postcode and language
        # queryset_list = queryset_list.filter(
        #     Q(electorate__icontains=destination.lower()) |
        #     Q(postcode__icontains=destination.lower())).filter(Q(language__icontains=language.lower()))

    # if there are no match, return the message
    if not queryset_list:
        error_msg = 'No Results'

    # return the result page
    return HttpResponse(render(request, template, {
        'error_msg': error_msg,
        'queryset_list': queryset_list,
        'curlocation': curlocation,
    }))


def calculateDistance(destination, location):
    # approximate radius of earth in k
    r = 6373.0

    lat1 = radians(float((destination.lat.strip())))
    lng1 = radians(float((destination.lng.strip())))
    lat2 = radians(float((location.lat.strip())))
    lng2 = radians(float((location.lng.strip())))

    dlng = lng2 - lng1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlng / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = r * c
    return distance

