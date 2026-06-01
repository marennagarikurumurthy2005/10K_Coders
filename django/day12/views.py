from django.shortcuts import render,redirect
from .models import College

# Create your views here.

def Create(request):
    if request.method=="POST":
        branch=request.POST.get('branch')
        hod=request.POST.get('hod')
        salary=request.POST.get('salary')
        staff=request.POST.get('staff')
        students=request.POST.get('students')

        College.objects.create(
            branch=branch,
            hod=hod,
            salary=salary,
            staff=staff,
            students=students
        )
        return redirect('details')

    return render(request,'add.html')


def Details(request):
    college=College.objects.all()
    return render(request,'details.html',{"college":college})

def Single(request,id):
    college=College.objects.get(id=id)
    return render(request,'singles.html',{'college':college})

def Delete(request,id):
    data=College.objects.get(id=id)
    data.delete()
    return  redirect('details')


def Update(request,id):
    data=College.objects.get(id=id)

    if request.method=='POST':
        branch=request.POST.get('branch')
        hod=request.POST.get('hod')
        salary=request.POST.get('salary')
        staff=request.POST.get('staff')
        students=request.POST.get('students')

        data.branch=branch
        data.hod=hod
        data.salary=salary
        data.staff=staff
        data.students=students
        data.save()
        return redirect('single',id=data.id)

    return render(request,'updates.html',{"college":data})
