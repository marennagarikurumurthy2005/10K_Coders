from django.db import models

# Create your models here.

class School(models.Model):
    stand=models.CharField( max_length=50)
    classroom=models.CharField(max_length=50)

class Standard(models.Model):
    # stand=models.CharField(max_length=50)
    # clsssroom=models.CharField(max_length=50)
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='standards')
    strength=models.IntegerField()
    teacher=models.CharField(max_length=50)
    cr=models.CharField(max_length=50)






