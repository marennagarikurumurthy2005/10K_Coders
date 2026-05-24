from rest_framework import serializers
from .models import Nirven

class NirvenSerializers(serializers.ModelSerializer):
    class Meta:
        model=Nirven
        fields='__all__'