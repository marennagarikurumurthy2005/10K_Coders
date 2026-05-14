from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def prime(request,num):
    primen=True
    for i in range(2,num):
        if num%i==0:
            primen=False
            break
    if primen:
        return HttpResponse(f"{num} is a prime number")
    else:
        return HttpResponse(f"{num} is not a prime number")
    
def login(request,username,password):
    user="python"
    passw="python123"
    if username==user and passw==password:
        return HttpResponse("login success")
    else:
        return HttpResponse("login failed")

