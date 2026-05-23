from django.shortcuts import render
from django.http import HttpResponse
from .models import mrits

# Create your views here.

def home(request):
    message="server started"

    students=mrits.objects.all()
    print(students)

    row=""
    for i in students:
        row+=f"""

                <tr>
                <td>{i.name}</td>
                <td>{i.email}</td>
                <td>{i.college}</td>
                <td>{i.branch}</td>
                </tr>
                """


    table=f"""
            <table style="border:1px solid">
            <tr>
            <thead>Name</thead>
            <thead>Email</thead>
            <thead>College</thead>
            <thead>Branch</thead>
            </tr>
            {row}
            </table>
                """


    return HttpResponse(table)
