from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.loginpage,name="loginpage"),
    path('check',views.getdata,name="getdata"),
]