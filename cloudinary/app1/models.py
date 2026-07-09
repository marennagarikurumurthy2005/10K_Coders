from django.db import models

# Create your models here.

class Surya_table(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()