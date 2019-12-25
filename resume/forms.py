from django import forms
from django.conf import settings
import requests


def recaptcha_validation(captcha_token):
    data = {
        'secret': settings.GOOGLE_RECAPTCHA_KEY,
        'response': captcha_token
    }

    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data).json()
    if 'success' in response:
        return response['success']

    return False


class ContactForm(forms.Form):
    def __init__(self, recaptcha=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.recaptcha = recaptcha

    name = forms.CharField(
        label='name',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Name',
            'class': 'form-control',
            'id': 'name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'youremail@example.com',
            'class': 'form-control',
            'id': 'email'
        })
    )
    subject = forms.CharField(
        label='subject',
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Subject',
            'class': 'form-control',
            'id': 'subject'
        })
    )
    message = forms.CharField(
        label='message',
        max_length=1000,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'message'
        })
    )

    def clean(self):
        super().clean()

        success = recaptcha_validation(self.recaptcha)
        if not success:
            raise forms.ValidationError('Invalid recaptcha!')

        return True
