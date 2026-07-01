from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
        # read_only_fields=['id']
        extra_kwargs={
            # 'age':{
            #     'write_only':True
            # },
            'username':{
                'required':False,
                'default':'default User'
            },
            'age':{
                'required':False,
                'default':25
            },
        }


        # validators 2 types 
        # 1.field level validator -> used to validate only one field

    def validate_age(self,age):
        if age <=18 or age>=55:
            raise serializers.ValidationError('employee age must be betqeen 19 and 54')
        return age

        #object level validation  :- used to validate morethan 1 fields
        #  here the data will be come as dictonary
    def validate(self,data):
        if data['username']=='default User' and data['age']==25:
            raise serializers.ValidationError("cannot add the employee with 2 default fields")
        return data
            

