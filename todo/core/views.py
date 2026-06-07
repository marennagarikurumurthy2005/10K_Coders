from django.shortcuts import render,redirect
from .models import todo,tododistory


# Create your views here.

def create(request):
    if request.method=="POST":
        name=request.POST.get('name')
        description=request.POST.get('description')
        priority=request.POST.get('priority')
        status=request.POST.get('status')

        todo.objects.create(
            name=name,
            description=description,
            priority=priority,
            status=status
        )
        return redirect('create')
    return render(request,'create.html')

def details(request):
    data=todo.objects.all()
    return render(request,'details.html',{'data':data})

def update(request,id):
    data=todo.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get('name')
        description=request.POST.get('description')
        priority=request.POST.get('priority')
        status=request.POST.get('status')

        data.name=name
        data.description=description
        data.priority=priority
        data.status=status

        data.save()
        return redirect('details')
    
    return render(request,'update.html',{'data':data})

def delete(request,id):
    data=todo.objects.get(id=id)
    tododistory.objects.create(
            name=data.name,
            description=data.description,
            priority=data.priority,
            status=data.status
    )
    data.delete()
    return redirect('details')

def history(request):
    data=tododistory.objects.all()
    return render(request,'history.html',{'data':data})

def pd(request,id):
    data=tododistory.objects.get(id=id)
    data.delete()
    return redirect('history')

def retrive(request,id):
    data=tododistory.objects.get(id=id)
    todo.objects.create(
            name=data.name,
            description=data.description,
            priority=data.priority,
            status=data.status
        )
    data.delete()
    return redirect('history')


