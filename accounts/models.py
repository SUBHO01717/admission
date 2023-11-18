from django.db import models
from django.contrib.auth.models import User
from backend.models import *

class UserProfile(models.Model):
    USER_ROLE = (('Staff', 'Staff'), ('Agent', 'Agent'), ('Student', 'Student'),('Partner', 'Partner'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userrole = models.CharField(max_length=20, choices=USER_ROLE,)
    user_pic = models.ImageField(upload_to="media/images", blank=True, null=True, default='default.jpg')
    phone = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=60, blank=True, null=True)
    state = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    represented_universities = models.ManyToManyField(University, related_name='partners', blank=True,)
    def __str__(self):
        return f"{self.user}- {self.userrole} "
        
   
