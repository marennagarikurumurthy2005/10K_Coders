from django.db import models
from django.conf import settings

class Faculty(models.Model):

    faculty_id = models.CharField(max_length=20)

    name = models.CharField(max_length=100)

    department = models.CharField(max_length=100)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name