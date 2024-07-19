from django import forms
from .models import Sake

class SakeForm(forms.ModelForm):
    class Meta:
        model = Sake
        fields = ['name', 'price', 'image']
