from django.shortcuts import render


# Create your views here.
def diet(request):
    return render(request, 'diet/diet.html', context={})