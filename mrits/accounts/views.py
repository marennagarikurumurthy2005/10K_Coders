from django.shortcuts import render
from .serializer import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class CusomTokenObtainView(TokenObtainPairView):
    serializer_class=CustomTokenObtainPairSerializer


