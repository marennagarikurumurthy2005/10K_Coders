from django.shortcuts import render
from django.http import HttpResponse
from .serializers import NirvenSerializers
from .models import Nirven

# Create your views here.

def home(request):

    nirven=Nirven.objects.all()
    serializer=NirvenSerializers(nirven,many=True)

    
    return HttpResponse(serializer.data)





