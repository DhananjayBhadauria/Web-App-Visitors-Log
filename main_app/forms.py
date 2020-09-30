from django.forms import ModelForm
from .models import *
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

class VisitorInfoUpdateForm(ModelForm):
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


class VisitAddForm(forms.ModelForm):
    class Meta:
        model = VisitDetails
        fields = ['visit_Date','Description']

        widgets ={
          
         
            'visit_Date':forms.TextInput(attrs={'readonly':'readonly','class':'form-control'}),
            'Description': forms.Textarea(attrs={'rows':3,'class':'form-control'})
        }

class OrganizationUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['fullName','photo']

        widgets = {
            'fullName':forms.TextInput(attrs={'class':'form-control'}),
            'photo': forms.FileInput(attrs={'class':'form-control'})
        }


class EditVisitForm(forms.ModelForm):
    class Meta:
        model = VisitDetails
        fields = ['Description']

        widgets ={
            'Description': forms.Textarea(attrs={'class':'form-control', 'rows':4})
        }
