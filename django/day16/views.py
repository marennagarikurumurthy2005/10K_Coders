from django.shortcuts import render,redirect,get_object_or_404
from .models import Cet
from .form import cetForm


# Create your views here.

def Createview16(request):
    form=cetForm()
    if request.method=="POST":
        form=cetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("stable")
        else:
            form=cetForm()
    
    return render(request,'cetform.html',{'form':form})

def DiaplayView16(request):
    data=Cet.objects.all()
    return render(request,'stable.html',{'data':data})

def UpdateView(request,id):
    obj=get_object_or_404(Cet,id=id)
    print(obj)
    form=cetForm(instance=obj)
    # form=cetForm(instance=id)
    if request.method=='POST':
        form=cetForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('stable')
        else:
            form=cetForm()
    return render(request,'updateform.html',{'form':form})

        

    
