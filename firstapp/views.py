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
query = (
    "insert into product(productname,price,category) values(%s,%s,%s)"  #  must be "s"
)
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
    product = request.POST.get("Product")
    price = request.POST.get("Price")
    category = request.POST.get("category")
    cursor.execute(query, [product, price, category])
    mydatabase.commit()
    return HttpResponse()


def insertdata(request):

    return render(request, "form.html")


def displaydata(request):
    # Connect to MySQL database
    with m.connect(
        host="localhost", user="root", password="Gourav@2806", database="pythondb1"
    ) as mydatabase:
        cursor = mydatabase.cursor()
        query = "SELECT * FROM product where category ='shirt'"
        cursor.execute(query)
        result = cursor.fetchall()

    return render(request, "display.html", {"result": result})
