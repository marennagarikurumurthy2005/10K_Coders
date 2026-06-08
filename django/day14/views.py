from django.shortcuts import render
from .models import*

# Create your views here.

def DataGet(request):
    data=Kukat.objects.select_related()
    return render(request,'visi.html',{'data':data})

