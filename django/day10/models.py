from django.db import models

# Create your models here.

class Palem(models.Model):
    name=models.CharField(max_length=50)
    ward=models.IntegerField()
    def __str__(self):
        return f"{self.name} {self.ward}"
