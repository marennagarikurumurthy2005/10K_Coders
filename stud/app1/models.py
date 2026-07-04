from django.db import models

# Create your models here.
class Users(models.Model):
    username=models.CharField(max_length=500)
    mail=models.EmailField(max_length=254)
    password=models.CharField(max_length=500)
    repassword=models.CharField(max_length=500)
    

class Students(models.Model):
    name=models.CharField(max_length=50)
    standard=models.IntegerField()
    fee_due=models.FloatField()