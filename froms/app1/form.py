from django import forms
from .models import Village

class villageForm(forms.ModelForm):
    class Meta:
        model=Village
        fields='__all__'