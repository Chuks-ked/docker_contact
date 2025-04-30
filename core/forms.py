from django import forms
from .models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fieds = ['name', 'email', 'message',]