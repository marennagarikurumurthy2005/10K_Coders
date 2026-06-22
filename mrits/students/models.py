from django.db import models
from django.conf import settings

# Create your models here.

class Student(models.Model):
    student_id=models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    course = models.CharField(max_length=100)

    email = models.EmailField()

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
