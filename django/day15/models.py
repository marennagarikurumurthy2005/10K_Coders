from django.db import models

# Create your models here.

class Institute(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    name=models.CharField(max_length=200)
    ins=models.ForeignKey(Institute,on_delete=models.CASCADE,null=True,blank=True)
    cou=models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name
    








    



