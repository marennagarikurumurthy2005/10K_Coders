from django.db import models

# Create your models here.
class Todomodel(models.Model):

    PRIORITY_CHOICE=[
        ('LOW','Low'),
        ('MEDIUM','Medium'),
        ('HIGH','High'),
    ]
    title=models.CharField(max_length=500)
    description=models.TextField(blank=True)
    priority=models.CharField(max_length=50,choices=PRIORITY_CHOICE,default="MEDIUM")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
