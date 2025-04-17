from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Welcome to first Django app")


def special(request):
    return HttpResponse("<b><u><i>Welcome to Special page</b></u></i>")
