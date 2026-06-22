from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICE=(
        ('student','Student'),
        ('faculty','Faculty'),
        ('admin','Admin'),
    )

    role=models.CharField(max_length=50,choices=ROLE_CHOICE)

    def __str__(self):
        return self.username
