from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.


# def home(request):
#     return HttpResponse("Welcome to first Django app")

import mysql.connector as m  # type: ignore

# database connectivity

mydatabase = m.connect(
    host="localhost", user="root", password="Gourav@2806", database="pythondb1"
)
query = "insert into person(name,address,age) values(%s,%s,%s)"  #  must be "s"
cursor = mydatabase.cursor()


def home(request):
    return render(request, "home.html")


def special(request):
    return HttpResponse("<b><u><i>Welcome to Special page</b></u></i>")


def vote(request, name, age):
    if age < 18:
        return JsonResponse({"message": "You cannot vote"})
    else:
        return JsonResponse({"message": "Most welcome for voting"})


def stn(request):
    products = {"list": ["Pen", "Notebook", "Marker", "Pencil"]}
    return render(request, "myhtml.html", products)


def elect(request):
    products = {"list": ["TV", "Laptop", "Mobile"]}
    return render(request, "myhtml.html", products)


def result(request):
    name = request.POST.get("name")
    address = request.POST.get("address")
    age = request.POST.get("age")
    cursor.execute(query, [name, address, age])
    mydatabase.commit()
    return HttpResponse()
