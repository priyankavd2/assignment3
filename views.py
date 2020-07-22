from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models
# Create your views here.

def loginpage(request):
    f1=forms.MyForms()
    return render(request,"login.html",{'form':f1})

def getdata(request):


    if request.method=="GET":
        un=request.GET['Username']
        p=request.GET['Password']
        pn=request.GET['Phonenumber']
        a=request.GET['Address']
        l1=models.studentinfo(Username=un,Password=p,Phonenumber=pn,Address=a)
        l1.save()
        return render(request,"valid.html",{"Username":un,"Password":p,"Phonenumber":pn,"Address":a})
    if request.method=="POST":
        un=request.POST['Username']
        p=request.POST['Password']
        pn=request.POST['Phonenumber']
        a=request.POST['Address']
        return render(request,"valid.html",{"Username":un,"Password":p,"Phonenumber":pn,"Address":a})