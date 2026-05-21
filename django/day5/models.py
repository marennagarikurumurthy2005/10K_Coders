from django.db import models

# Create your models here.

class murthy(models.Model):
    name=models.CharField( max_length=50)
    num=models.IntegerField()
    adds=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name},{self.num},{self.adds}"
