from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import StudentSerializer
from .models import Student
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class StudentViewSet(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        user=self.request.user
        if user.role=='student':
            return Student.objects.filter(user=user)
        return Student.objects.all()

