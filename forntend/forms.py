from django.forms import ModelForm
from . models import *
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = UserMessage
        fields="__all__"
        widgets = {
          'message': forms.Textarea(attrs={'rows':4,}),
        }