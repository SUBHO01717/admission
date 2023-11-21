from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField 
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Intake(models.Model):
    name = models.CharField(max_length=100)
    start_from = models.CharField(max_length=20, blank=True,null=True)
    end_at = models.CharField(max_length=20, blank=True,null=True)

    def __str__(self):
        return f"{self.name}"


class University(models.Model):
    COUNTRY_LIST=(("UK","UK"),("USA","USA"))
    TYPE_LIST=(("University","University"),("School","School"),("College","College"))
    ACCEPTED_LIST=(("Home","Home"),("Foreign","Foreign"),("Both","Both"))
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='media',blank=True, null=True )
    intakes=models.ManyToManyField(Intake)
    country=models.CharField(choices=COUNTRY_LIST, max_length=30,default=None)
    accept_student=models.CharField(choices=ACCEPTED_LIST, max_length=30,default=None, blank=True, null=True)
    type=models.CharField(choices=TYPE_LIST, max_length=30,default=None, blank=True, null=True)
    deatils=RichTextField(blank=True,null=True)
    image = models.ImageField(upload_to='media', blank=True, null=True)
   
    
    def __str__(self):
        return self.name

class Campus(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='media', blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    stree = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100,blank=True, null=True)
    state=models.CharField(max_length=100,blank=True, null=True)
    zip_code=models.CharField(max_length=100, blank=True, null=True)
    country=models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class DegreeLevel(models.Model):
    name=models.CharField(max_length=20,null= True, blank=True)
    def __str__(self):
        return f"{self.name}"

class EducationArea(models.Model):
    name=models.CharField(max_length=20,null= True, blank=True)
    def __str__(self):
        return f"{self.name}"
    
class Course(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    area_education = models.ForeignKey(EducationArea, on_delete=models.SET_NULL, null=True, blank=True)
    degree_level = models.ForeignKey(DegreeLevel,on_delete=models.SET_NULL, null=True, blank=True)
    duration = models.CharField(max_length=100)  # Duration in months
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    Local_fees = models.DecimalField(max_digits=10, decimal_places=2, null= True, blank=True)
    details=RichTextField(blank=True,null=True)
    intakes=models.ManyToManyField(Intake)
    def __str__(self):
        return f"{self.name}"

class Application(models.Model):
    APPLICATION_STAT=(("Approved","Approved"),("Rejected","Rejected"),("On Process","On Process"), ("Pending","Pending"),("Returned","Returned"))
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    intake = models.ForeignKey(Intake, on_delete=models.CASCADE)
    ssc_certificate=models.FileField(upload_to='media/files', blank=True, null=True)
    hsc_certificate=models.FileField(upload_to='media/files', blank=True, null=True)
    bachelor_certificate=models.FileField(upload_to='media/files', blank=True, null=True)
    ielts_certificate=models.FileField(upload_to='media/files', blank=True, null=True)
    statement=models.FileField(upload_to='media/files', blank=True, null=True)
    application_status=models.CharField(choices=APPLICATION_STAT, max_length=30,default="Pending")
    application_date=models.DateField(auto_now_add=True, blank=True,null=True)
    messages=models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.applicant} - {self.course} - {self.university}-{self.application_status}"

class AgentApplication(models.Model):
    APPLICATION_STAT=(("Approved","Approved"),("Rejected","Rejected"),("On Process","On Process"), ("Pending","Pending"),("Returned","Returned"))
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    student_name=models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    intake = models.ForeignKey(Intake, on_delete=models.CASCADE)
    ssc_certificate=models.FileField(upload_to='media/files', blank=True, null=True)
    hsc_certificate=models.FileField(upload_to='media/files', blank=True, null=True)
    bachelor_certificate=models.FileField(upload_to='media/files', blank=True, null=True)
    ielts_certificate=models.FileField(upload_to='media/files', blank=True, null=True)
    statement=models.FileField(upload_to='media/files', blank=True, null=True)
    application_status=models.CharField(choices=APPLICATION_STAT, max_length=30,default="Pending")
    application_date=models.DateField(auto_now_add=True,blank=True, null=True)
    messages=models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.applicant} - {self.course} - {self.university}-{self.application_status}"
    
class BookApointment(models.Model):
    BOOKING_STATUS=(("Accepted","Accepted"),("Reject","Reject"),("Cancelled","Cancelled"),)
    email = models.EmailField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE, blank=True, null=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, blank=True, null=True)
    date=models.DateField()
    note=models.TextField(max_length=500, blank=True, null=True)
    status=models.CharField(choices=BOOKING_STATUS, max_length=30,default="Accepted" )

    def __str__(self):
        return f"{self.email}"
    

