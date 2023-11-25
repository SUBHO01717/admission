from django.forms import ModelForm
from . models import *
from django import forms
from ckeditor.widgets import CKEditorWidget

class ContactForm(ModelForm):
    class Meta:
        model = UserMessage
        fields="__all__"
        widgets = {
          'message': forms.Textarea(attrs={'rows':4,}),
        }
        
class EventForm(ModelForm):
    class Meta:
        model = Events
        fields = "__all__"
        widgets = {
            'event_date': forms.DateInput( attrs={'class': 'form-control','type': 'date' }),
        }
        
class BlogForm(ModelForm):
    class Meta:
        model = BlogNews
        fields = "__all__"
        widgets = {
            'date': forms.DateInput( attrs={'class': 'form-control','type': 'date' }),
        }
        details = forms.CharField(widget = CKEditorWidget())