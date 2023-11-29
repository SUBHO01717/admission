from django.forms import ModelForm, HiddenInput
from accounts.models import *
from .models import *
from django import forms
from ckeditor.widgets import CKEditorWidget

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email" ]
        widgets = {
            "email": forms.TextInput(attrs={"readonly": "readonly"}),
        }

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ["userrole", "user_pic", "phone", "address", "city", "state", "country"]
        widgets = {
            "userrole": forms.TextInput(attrs={"readonly": "readonly"}),
        }

class UniversityForm(ModelForm):
    class Meta:
        model = University
        fields = "__all__"
        
class CampusForm(ModelForm):
    class Meta:
        model = Campus
        fields = "__all__"

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        details = forms.CharField(widget = CKEditorWidget())
        
class StudentAppForm(ModelForm):
    class Meta:
        model = Application
        exclude=["applicant"]
        widgets = {
            "applicant": forms.Select(attrs={"readonly": "readonly"}),
        }

 


class AgentAppForm(ModelForm):
  
    class Meta:
        model = AgentApplication
        exclude=["applicant"]
        widgets = {
            "applicant": forms.Select(attrs={"readonly": "readonly"}),
        }
        



class StudentAppCreate(ModelForm):
    class Meta:
        model = Application
        fields = "__all__"

class AgentAppForm2(ModelForm):
  
    class Meta:
        model = AgentApplication
        exclude=["applicant", "application_status"]

class StudentAppForm2(ModelForm):
    class Meta:
        model = Application
        exclude=["applicant", "application_status"]
        
        


        

       