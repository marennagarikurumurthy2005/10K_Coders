from django.db import models

# Create your models here.

class mrits(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254,unique=True)
    college=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.branch}"
    
    
    


