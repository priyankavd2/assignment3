from django.db import models

# Create your models here.
class studentinfo(models.Model):
       Username=models.CharField(max_length=100)
       Password=models.CharField(max_length=100)
       Phonenumber=models.CharField(max_length=10)
       Address=models.CharField(max_length=100)