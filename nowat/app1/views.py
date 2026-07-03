from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Features
from .serializer import FeatureSerializer
import json

# Create your views here.

@csrf_exempt
def create(request):
    raw_data=json.loads(request.body)
    serializer_data=FeatureSerializer(data=raw_data)
    if serializer_data.is_valid():
        serializer_data.save()
        return JsonResponse({'statues':"data created"})
    return JsonResponse(serializer_data.errors)


@csrf_exempt
def update(request,id):
    re_data=json.loads(request.body)
    print(re_data)
    print(id)
    try:
        data=Features.objects.get(id=id)
        # print(data)
        if data:
            new_data=FeatureSerializer(re_data,data,partial=True)
            new_data.save()
            return JsonResponse({"status":"data updated"})
    except:
        return JsonResponse({'status':"data not found with this id"})


@csrf_exempt
def delete(request,id):
    try:
        data=Features.objects.get(id=id)
        if data:
            data.delete()
            return JsonResponse({'status':"data deleted"})
    
    except:
        return JsonResponse({'status':"data not found with this id"})
    
        
    



