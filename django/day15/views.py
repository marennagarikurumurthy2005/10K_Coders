from django.shortcuts import render
from .models import Institute,Course,Student

# Create your views here.


def DisView(request):
    data=Student.objects.all()

    return render(request,'dump.html',{'data':data})
