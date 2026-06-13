from django.shortcuts import render,redirect,get_object_or_404
from .models import Village
from .form import villageForm


# Create your views here.


def Formv(request):
    form=villageForm()
    if request.method=="POST":
        form=villageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details')
        else:
            form=villageForm()
    return render(request,'form.html',{'form':form})

def Details(request):
    form=Village.objects.all()
    return render(request,'details.html',{'form':form})


def Update(request,id):
    obj=get_object_or_404(Village,id=id)
    form=villageForm(instance=obj)
    if request.method=='POST':
        form=villageForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('details')
        else:
            form=villageForm()
    return render(request,'update.html',{'form':form})

def Delete(request,id):
    obj=get_object_or_404(Village,id=id)
    obj.delete()
    return redirect('details')
