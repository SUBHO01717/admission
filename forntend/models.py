from django.db import models
from ckeditor.fields import RichTextField 
# Create your models here.


class UserMessage(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.TextField()
    
    def __str__(self):
        return self.email
    
class Events(models.Model):
    event_date=models.DateField()
    image=models.ImageField(upload_to='media',blank=True, null=True)
    title=models.CharField(max_length=100)  
    address=models.CharField(max_length=100)
    event_link=models.CharField( max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.title

class BlogNews(models.Model):
    date=models.DateField()
    title=models.CharField(max_length=100)  
    details=RichTextField(blank=True,null=True)
    def __str__(self):
        return self.title