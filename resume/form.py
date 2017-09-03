from django.forms import ModelForm
from resume.models import Contact
from django import forms

class ContactModelForm(ModelForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True)
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
