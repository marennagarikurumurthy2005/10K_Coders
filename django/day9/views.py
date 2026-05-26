from django.shortcuts import render,redirect
from .models import Ipl

# Create your views here.

def create(request):
    if request.method=="POST":
        name=request.POST.get("name")
        seat=request.POST.get("seat")
        stand=request.POST.get("stand")

        Ipl.objects.create(
            name=name,
            seat=seat,
            stand=stand
        )

        return redirect("details")
    return render(request,'ipl.html')

def details(request):
    ipl=Ipl.objects.all()
    return render(request,'seating.html',{"ipl":ipl})
    

