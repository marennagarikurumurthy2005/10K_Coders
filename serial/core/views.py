import json
from django.shortcuts import render, HttpResponse
from .models import Employee
from django.http import JsonResponse
import bcrypt
from django.views.decorators.csrf import csrf_exempt
from .serializer import EmployeeSerializer
from .passwords import paw_hashing


# Create your views here.



@csrf_exempt
def create(request):
    request_data = json.loads(request.body)
    request_data['password']=paw_hashing(request_data['password'])
    ser_data=EmployeeSerializer(data=request_data)
    if ser_data.is_valid():
        ser_data.save()
        return JsonResponse({"status":"employee saved in DB"})
    else:
        return JsonResponse(ser_data.errors)
    

@csrf_exempt
def login(request):
    requested_data = json.loads(request.body)
    username = requested_data['username']
    password = requested_data['password']
    # print(username,password)
    encoded=password.encode('utf-8')
    try:
        db_data=Employee.objects.get(username=username)
        data=EmployeeSerializer(db_data).data
    except Employee.DoesNotExist:
        return JsonResponse({"response": "user not found"})
    db_password = db_data.password.encode('utf-8')
    
    if bcrypt.checkpw(encoded,db_password):
        response= JsonResponse(
              {
            'response': {
                'username':data['username'],
                'name':data['name'],
                # 'age':data['age'],
            }
        }    
        )
        response.set_cookie(
            key='is_login',
            value=True,
            max_age=60
        )
        return response
    return JsonResponse({'response':'password incorrect'})


@csrf_exempt
def home(request):
    if bool(request.COOKIES.get('is_login')):
        return JsonResponse({'status':"welcome to dashboard"})
    return JsonResponse({'status':"Login cheyra hooka😁"})


