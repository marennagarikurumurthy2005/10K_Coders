from django.db import models

# Create your models here.

class College(models.Model):
    branch=models.CharField(max_length=50)
    hod=models.CharField( max_length=50)
    salary=models.FloatField()
    staff=models.FloatField()
    students=models.IntegerField()

class History(models.Model):
    branch=models.CharField(max_length=50)
    hod=models.CharField( max_length=50)
    salary=models.FloatField()
    staff=models.FloatField()
    students=models.IntegerField()



    

