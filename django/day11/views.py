from django.shortcuts import render,redirect
from .models import Employee

# Create your views here.

def Home(request):
    if request.method=="POST":
        name=request.POST.get("name")
        dept=request.POST.get("dept")
        age=request.POST.get("age")
        salary=request.POST.get("salary")

        Employee.objects.create(
            name=name,
            dept=dept,
            age=age,
            salary=salary
            
        )
        return redirect("details")
    return render(request,"emp.html")

def Details(request):
    emp=Employee.objects.all()
    return render(request,'tab.html',{"emp":emp})

def Single(request,id):
    emp=Employee.objects.get(id=id)
    return render(request,"single.html",{"emp":emp})

def Update(request,id):
    emp=Employee.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("name")
        dept=request.POST.get("dept")
        age=request.POST.get("age")
        salary=request.POST.get("salary")

        emp.name=name
        emp.dept=dept
        emp.age=age
        emp.salary=salary
        emp.save()

        return redirect('single',id=emp.id)
    return render(request,'update.html',{'emp':emp})

def Delete(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('details')