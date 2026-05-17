from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def details(request):
    names=["MK","RK","VK"]
    ages=[21,23,38]
    
    row=""

    for i in range(len(names)):
        row=row+f"<tr ><td >{names[i]}</td><td >{ages[i]}</td></tr >"


    table=f"""
        <table>
        <tr>
        <thead>Name</thead>
        <thead>Age</thead>
        </tr>
        <tr >
        {row}
        </tr>
        </table>
        """
    
    return HttpResponse(table)

def home(request):
    return HttpResponse("server started")

def name(request):
    return HttpResponse("this is name page")

def num(request):
    return HttpResponse("this is number page")

def branch(request):
    return HttpResponse("this is branch page")

def year(request):
    return HttpResponse("this is year page")

def father(request):
    return HttpResponse("thi is  father's page")

def mother(request):
    return HttpResponse("this is mother's page")

def sister(request):
    return HttpResponse(" this is sister's page")

def gp(request):
    return HttpResponse("this is grandparents page")

def adds(request):
    return HttpResponse(" this is address page")

def registration(request):
    return HttpResponse("welcome to register page")
