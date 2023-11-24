from django.urls import path

from . views import *

urlpatterns = [
    path('',Home,name="index"),
    path('about-us',AboutUs,name="about-us"),
    path('why_UK',StudyUK,name="why_UK"),
    path('news_and_blogs',NewsBlogs,name="news_and_blogs"),
    path('events',Events,name="events"),
    path('students',Student,name="students"),
    path('recruitment_partner',Recruiter,name="recruitment_partner"),
    path('institutional_partner',Partner,name="institutional_partner"),
    path('terms_conditions',TermsConditions,name="terms_conditions"),
    path('why_usa',StudyUsa,name="why_usa"),
    path('application_process',ApplicationProcess,name="application_process"),
    path('application_process_uk_local',ApplicationProcessLocal,name="application_process_uk_local"),
    path('application_process_usa',ApplicationProcessUSA,name="application_process_usa"),
    path('why_us',WhyUs,name="why_us"),
    path('uk_Institutions',UKInstitutions,name="uk_Institutions"),
    path('uk_Institutions/institution/<str:institution_type>/', UKInstitutions, name='filtered_university_list_institution'),
    path('uk_Institutions/accepted/<str:Accepted>/', UKInstitutions, name='filtered_university_list_accepted'),

   
    path('uk_universities',UkUniversities,name="uk_universities"),
    path('uk_colleges',UKColleges,name="uk_colleges"),
    path('usa_universities',USAUniversities,name="usa_universities"),
    path('universrity_details/<int:pk>/',UniversrityDetails,name="universrity_details"),
    path('course_details/<int:pk>/',DetailCourse,name="course_details"),
    path('contact_us',ContactUs,name="contact_us"),
  
]
