from django.db import models
# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=500)
    age=models.IntegerField()
    username=models.CharField(max_length=500)
    password=models.CharField(max_length=500)

    def __str__(self):
        return self.name
    

