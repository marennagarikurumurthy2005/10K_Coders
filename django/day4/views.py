from django.shortcuts import render

# Create your views here.

data={}
def home(request):
    username=request.POST.get('username')
    email=request.POST.get('email')
    data={"name":username,"email":email}
    return render(request,"login.html",data)

def redirect(request):

    return render(request,"direct.html",data)




