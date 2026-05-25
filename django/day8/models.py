from django.db import models

# Create your models here.

class Ten(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.IntegerField()
    cgpa=models.FloatField()

    def __str__(self):
        return f"{self.name} {self.rollno} {self.cgpa}"
    
