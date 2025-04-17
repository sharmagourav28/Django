from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.


# def home(request):
#     return HttpResponse("Welcome to first Django app")


def home(request):
    return render(request, "myhtml.html")


def special(request):
    return HttpResponse("<b><u><i>Welcome to Special page</b></u></i>")


def vote(request, name, age):
    if age < 18:
        return JsonResponse({"message": "You cannot vote"})
    else:
        return JsonResponse({"message": "Most welcome for voting"})
