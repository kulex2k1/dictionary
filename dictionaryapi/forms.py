from django import forms 
from django.forms import ModelForm

from .models import Dict_word


class DictForm(forms.ModelForm):
    
    class Meta:
        model = Dict_word
        fields = '__all__'
