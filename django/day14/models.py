from django.db import models

# Create your models here.


class Kukat(models.Model):
    vlg=models.CharField(max_length=50)

    def __str__(self):
        return self.vlg
    
class Col(models.Model):
    col=models.CharField(max_length=50)
    vlgf=models.ForeignKey(Kukat,on_delete=models.CASCADE,null=True, blank=True,related_name='t2')

    def __str__(self):
        return self.col
    
class vr(models.Model):
    name=models.CharField(max_length=50)
    vlgfr=models.ForeignKey(Kukat,on_delete=models.CASCADE,null=True,blank=True,related_name='t3')

    def __str__(self):
        return self.name


