from django.db import models

# Create your models here.

class Ipl(models.Model):
    name=models.CharField(max_length=50)
    seat=models.IntegerField()
    stand=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.seat} {self.stand}"

