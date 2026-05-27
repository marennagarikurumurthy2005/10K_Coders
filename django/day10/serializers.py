from rest_framework import serializers
from .models import Palem

class palemSerializers(serializers.ModelSerializer):
    class Meta:
        model=Palem
        fields='__all__'