from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from .models import Employee


def index(request):
    employee_list = Employee.objects.all()
    context = {'employee_list': employee_list}
    return render(request, 'firstapp/index.html', context=context)

# from .db import getconnection

# conn = getconnection()

# Create your views here.
# def home(request):
#     return HttpResponse("Welcome to first Django app")



# # database connectivity
# mydatabase = m.connect(
#     host="localhost", user="root", password="Gourav@2806", database="pythondb1"
# )

# query = (
#     "insert into product(productname,price,category) values(%s,%s,%s)"  #  must be "s"
# )
# cursor = conn.cursor()


# def home(request):
#     return render(request, "home.html")


# def special(request):
#     return HttpResponse("<b><u><i>Welcome to Special page</b></u></i>")


# def vote(request, name, age):
#     if age < 18:
#         return JsonResponse({"message": "You cannot vote"})
#     else:
#         return JsonResponse({"message": "Most welcome for voting"})


# def stn(request):
#     products = {"list": ["Pen", "Notebook", "Marker", "Pencil"]}
#     return render(request, "myhtml.html", products)


# def elect(request):
#     products = {"list": ["TV", "Laptop", "Mobile"]}
#     return render(request, "myhtml.html", products)


# def result(request):
#     product = request.POST.get("Product")
#     price = request.POST.get("Price")
#     category = request.POST.get("category")
#     cursor.execute(query, [product, price, category])
#     conn.commit()
#     return HttpResponse()


# def insertdata(request):

#     return render(request, "form.html")


# def displaydata(request):
#     # Connect to MySQL database
#     with m.connect(
#         host="localhost", user="root", password="Gourav@2806", database="pythondb1"
#     ) as mydatabase:
#         cursor = mydatabase.cursor()
#         query = "SELECT * FROM product where category ='shirt'"
#         cursor.execute(query)
#         result = cursor.fetchall()

#     return render(request, "display.html", {"result": result})


# def displaydata(request):
#     conn = getconnection()
#     cursor = conn.cursor()

#     # If you want to filter only 'shirt' category
#     query = "SELECT * FROM product WHERE category = %s"
#     cursor.execute(query, ("shirt",))  # Note the comma to make it a tuple
#     result = cursor.fetchall()

#     conn.close()
#     return render(request, "display.html", {"result": result})



#18/april
# def home_view(request):
#     return render(request, "home18.html")

# def login_view(request):
#     return render(request,"login.html")

# #18/april
# def result18(request):
#     uname = request.POST.get('uname')
#     password = request.POST.get('password')
#     if (uname == 'scott' and password == 'tiger'):
#         return render(request, "welcome.html", {'username': uname})
#     else:
#         return render(request, "error.html")



# def home(request):
#     return render(request, "home18_1.html")

# def national(request):
#     return render(request, "National.html")

# def international(request):
#     return render(request, "International.html")
#
# def home(request):
#     return render(request,'home_11.html')
#
# def shop(request):
#     return render(request, 'shop.html')
#
# def addCart(request):
#     items = request.POST.getlist('product')
#     if request.session.get("prodlist"):
#         mylist=request.session.get("prodlist")
#         mylist.extend(items)
#         request.session['prodlist']=mylist
#     else:
#         request.session['prodlist']=items
#     return render(request, 'home_11.html')
#
#
# def viewCart(request):
#     if request.session.get("prodlist"):
#         mylist=request.session.get("prodlist")
#         return render(request, 'viewCart.html',{'itemlist':mylist})
#     else:
#         return render(request,'Empty.html')
#
# def payment(request):
#     # as if we receive payment here
#
#     del request.session['prodlist']  # remove the key 'prodlist' and its associated value from the session.
#
#     """
# 	or you can delete entire session
#      request.session.flush()  # Deletes the session data and the session ID
#     """
#
#     return render(request, 'welcome1.html')



   
