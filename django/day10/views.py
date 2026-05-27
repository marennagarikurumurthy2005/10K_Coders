from django.shortcuts import render,redirect
from .models import Palem
from django.http import HttpResponse,response
from .serializers import palemSerializers


# Create your views here.

def Home(request):
    if request.method=="POST":
        name=request.POST.get("name")
        ward=request.POST.get("ward")

        Palem.objects.create(
            name=name,
            ward=ward
        )

        return redirect("display")
    
    return render(request,"inp.html")

def Display(request):
    data=Palem.objects.all()
    palemData=palemSerializers(data,many=True)
    return HttpResponse(palemData.data)
    



