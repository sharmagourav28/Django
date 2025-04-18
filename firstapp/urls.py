"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# we got error on this line
from . import views  # we have to place . means current folder
from django.contrib import admin
from django.urls import path

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", views.home, name="home page"),
#     path("special/", views.special, name="special page"),
#     # path("voting/<str:name>/<int:age>/", views.vote, name="voting page"),
#     # path("Stationery/", views.stn, name="Stationery page"),
#     # path("Electronics/", views.elect, name="Electronics page"),
#     path("insertdata/", views.insertdata, name="insert value"),
#     path("displaydata/", views.displaydata, name="Display value"),
#     path("go", views.result, name="view page"),
# ]

# server gets automaticallt updated
# http://127.0.0.1:8000/  default port number is 8000
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',views.home_view,name='home page'),
    # path('login',views.login_view,name='login page'),
    # path('go',views.result18,name='result page')


    #header and footer
    # path('admin/', admin.site.urls),
    # path('',views.home,name="home page"),
    # path('national',views.national,name='national page'),
    # path('international',views.international,name='international page')


    #Session
     path('admin/', admin.site.urls),
    # path('',views.home,name="home page"),
    path('', views.index, name='index'),
    # path('addCart',views.addCart,name="add cart"),
    # path('shopping',views.shop,name='shop'),
    # path('viewCart',views.viewCart,name='view cart'),
    # path('payment',views.payment,name='view cart')
    # sqlalcemy
    path('student/', views.student_view),
]

