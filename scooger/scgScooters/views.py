from django.shortcuts import render

# Create your views here.


def scootersHome(request):
    return render(request, "scgScooters/scgScooters.html")
