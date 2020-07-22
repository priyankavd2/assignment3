from django import forms

class MyForms(forms.Form):
    Username=forms.CharField(label="Username",max_length=100)
    Password=forms.CharField(label="Passsword",max_length=100) 
    Phonenumber=forms.CharField(label="Phonenumber",max_length=100)
    Address=forms.CharField(label="Address",max_length=100)