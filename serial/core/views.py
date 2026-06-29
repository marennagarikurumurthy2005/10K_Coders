import json
from django.shortcuts import render, HttpResponse
from .models import Employee
from django.http import JsonResponse
import bcrypt
from django.views.decorators.csrf import csrf_exempt
from .serializer import EmployeeSerializer

# Create your views here.



@csrf_exempt
def create(request):
    request_data = json.loads(request.body)
    password_from_request = request_data['password'].encode('utf-8')
    salt = bcrypt.gensalt(rounds=12)
    request_data['password'] = bcrypt.hashpw(password_from_request,salt).decode('utf-8')
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
    except Employee.DoesNotExist:
        return JsonResponse({"response": "user not found"})
    db_password = db_data.password.encode('utf-8')
    if bcrypt.checkpw(encoded,db_password):
        return JsonResponse(
              {
            'response': {
                'username': db_data.username,
                'name': db_data.name,
                'age': db_data.age
            }
        }    
        )
    return JsonResponse({'response':'password incorrect'})


@csrf_exempt
def update(request):
    pass

