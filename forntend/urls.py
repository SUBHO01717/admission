from django.urls import path

from . views import *

urlpatterns = [
    path('',Home,name="index"),
    path('about-us',AboutUs,name="about-us"),
    path('why_UK',StudyUK,name="why_UK"),
    path('why_usa',StudyUsa,name="why_usa"),
    path('application_process',ApplicationProcess,name="application_process"),
    path('application_process_usa',ApplicationProcessUSA,name="application_process_usa"),
    path('why_us',WhyUs,name="why_us"),
    path('uk_universities',UkUniversities,name="uk_universities"),
    path('usa_universities',USAUniversities,name="usa_universities"),
    path('universrity_details/<int:pk>/',UniversrityDetails,name="universrity_details"),
    path('course_details/<int:pk>/',DetailCourse,name="course_details"),
    path('contact_us',ContactUs,name="contact_us"),
  
]
