# -------------------------------------------------
# scgFactory
# -------------------------------------------------

"""
This page will register RFID readers to scooters
is intended for factory users to use - 
stupid idea to do it through web.
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def factoryFloor(request):
    print("Factory floor requested")
    if not request.user.is_authenticated:
        print("User is not authenticated, redirecting to login")
        messages.error(request, f"You need to log in to access this page")
        return redirect('login')

    else:
        if not isFactory(request):
            messages.error(request, f"You have no right to access this page")
            return redirect('login')
        else:
            return render(request, "scgFactory/floor.html")


def rfidRoom(request):
    print("Rfidroom requested")
    return render(request, "scgFactory/rfidroom.html")


def isFactory(request):
    user_group = request.user.groups.values_list('name', flat=True)
    isAllowed = True
    print(user_group)
    return isAllowed
