from django.shortcuts import render

# Create your views here.
def healthcare(request):
    return render(request, 'healthcare/healthcare.html', context={})


def system(request):
    return render(request, 'healthcare/system.html', context={})


def cost(request):
    return render(request, 'healthcare/cost.html', context={})


def waiting(request):
    return render(request, 'healthcare/waiting.html', context={})


def translation(request):
    return render(request, 'healthcare/translation.html', context={})

