from rest_framework import serializers
from .models import Surya_table

class Suryaserializer(serializers.ModelSerializer):
    class Meta:
        model = Surya_table
        fields = '__all__'