from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.


def login_request(request):
    return redirect("/accounts/login/")  # Nosūtām uz allAuth


# Tiek izsaukts logouts.
def logout_request(request):
    return redirect("/accounts/logout/")  # Nosūtām uz allAuth


def register_request(request):
    #print(f"register request")
    return redirect("/accounts/signup/")  # Nosūtām uz allAuth


def scgUserProfile(request):
    return render(request, "scgUsers/profile.html")
