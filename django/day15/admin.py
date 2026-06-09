from django.contrib import admin
from .models import Institute,Student,Course

# Register your models here.

admin.site.register(Institute)
admin.site.register(Course)
admin.site.register(Student)
