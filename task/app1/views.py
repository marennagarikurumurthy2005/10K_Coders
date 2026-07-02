from django.shortcuts import render 
from django.http import JsonResponse
import json
from .models import Todomodel
from .serializer import TodomodelSerializer
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def create(request):
    raw_data=json.loads(request.body)
    sdata=TodomodelSerializer(data=raw_data)
    if sdata.is_valid():
        sdata.save()
        return JsonResponse({"status":"todo created"})
    return JsonResponse(sdata.errors)
    
def update(request,id):
    pass

def delete(request,id):
    pass


def home(request):
    data=Todomodel.objects.all()
    serial=TodomodelSerializer(data,many=True,)
    if data.exists():
        return JsonResponse(serial.data,safe=False)
    return JsonResponse({"message":"No todo is present......!"})


