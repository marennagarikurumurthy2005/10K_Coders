from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse


# Create your views here.

def Create(request):
    if request.method=='POST':
        stand=request.POST.get('stand')
        classroom=request.POST.get('class')
        strength=request.POST.get('strength')
        teacher=request.POST.get('teacher')
        cr=request.POST.get('cr')

        school=School.objects.create(
            stand=stand,
            classroom=classroom
        )

        Standard.objects.create(
            school=school,
            strength=strength,
            teacher=teacher,
            cr=cr
        )
        return redirect('display')
    return render(request,'from.html')

def Display(request):
    

    standard=Standard.objects.all()

   


    return render(request,'view.html',{'data':standard})


    


