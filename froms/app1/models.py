from django.db import models

# Create your models here.

class Village(models.Model):
    doornum=models.CharField(max_length=50,unique=True,null=False)
    mem=models.IntegerField()
    famhead=models.CharField(max_length=50)
    income=models.IntegerField()

    def __str__(self):
        return self.doornum

class HistoryData(models.Model):
    doornum=models.CharField(max_length=50,unique=True,null=False)
    mem=models.IntegerField()
    famhead=models.CharField(max_length=50)
    income=models.IntegerField()

    def __str__(self):
        return self.doornum

    

