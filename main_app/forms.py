from django.forms import ModelForm
from .models import Visitor
from django import forms

class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        fields = ['full_Name','contact_Number','alternate_Contact_Number','email','address']

        widgets = {
            'address': forms.Textarea(attrs={'rows': 3, 'class':'form-control form-control-sm'}),
            'full_Name': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'contact_Number':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'email':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'alternate_Contact_Number':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            
           
        }