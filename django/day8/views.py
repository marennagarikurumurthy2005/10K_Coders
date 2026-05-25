from django.shortcuts import render
from .models import Ten

# Create your views here.

def home(request):
    if request.method=="POST":
        name=request.POST.get("name")
        rollno=request.POST.get("rollno")
        cgpa=request.POST.get("cgpa")

        Ten.objects.create(
            name=name,
            rollno=rollno,
            cgpa=cgpa
        )
    
    data=Ten.objects.all()






    return render(request,'data.html',{"data":data})
