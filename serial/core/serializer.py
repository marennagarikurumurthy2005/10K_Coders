from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
        read_only_fields=['id']
        extra_kwargs={
            'age':{
                'write_only':True
            },
            'username':{
                'required':False,
                'default':'default User'
            }
        }