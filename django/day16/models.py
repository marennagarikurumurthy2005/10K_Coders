from django.db import models

# Create your models here.


class Cet(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.TextField()

    def __str__(self):
        return f"{self.name} {self.age} {self.address}"

