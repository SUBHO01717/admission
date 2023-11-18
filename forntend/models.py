from django.db import models

# Create your models here.


class UserMessage(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.TextField()
    
    def __str__(self):
        return self.email