from rest_framework import serializers
from .models import Users,Students


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields='__all__'
    
    def validate(self, attrs):
        if attrs['password']!=attrs['repassword']:
            raise serializers.ValidationError('password does not matched')
        return attrs


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields='__all__'

