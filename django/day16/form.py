from django import forms
from .models import Cet

class cetForm(forms.ModelForm):
    class Meta:
        model = Cet
        fields = '__all__'
    