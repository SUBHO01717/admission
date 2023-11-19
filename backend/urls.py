from django.urls import path
from . views import *


urlpatterns = [
  
   path('userprofile',Profile,name="userprofile"),
   path('userprofile_edit/',ProfileEdit,name="userprofile_edit"),
   path('university/<int:pk>/', UniversityDetails, name='university'),
   path('courseDetails/<int:pk>/', CourseDetails, name='courseDetails'),
   
   path('agentedit/<int:pk>/', AgentEdit, name='agentedit'),
   path('agentdelete/<int:pk>/', DeleteProfile, name='agentdelete'),
   
   path('partner_edit/<int:pk>/', PartnerEdit, name='partner_edit'),
   path('partner_delete/<int:pk>/', DeleteProfile, name='partner_delete'),
   
   path('studentdelete/<int:pk>/', DeleteProfile, name='studentdelete'),
   path('studentedit/<int:pk>/', StudentEdit, name='studentedit'),
   
   path('create_university/', CreateUniversity, name='create_university'),
   path('edit_university/<int:pk>/', EditUniversity, name='edit_university'),
   path('create_campus/', CreateCampus, name='create_campus'),
   path('edit_campus/<int:pk>/', EditCampus, name='edit_campus'),
   path('course_create/', CreateCourse, name='course_create'),
   path('course_edit/<int:pk>/', CourseEdit, name='course_edit'),
   path('course_delete/<int:pk>/', DeleteCourse, name='course_delete'),
   
   path('student_application_create/', StudentApplicationCreateBlank, name='student_application_create2'),
   path('student_application_create/<int:university_id>/<int:course_id>/', StudentApplicationCreate, name='student_application_create'),
   path('student_application/<int:pk>/', StudentAppDetails, name='student_application'),
   path('student_application_edit/<int:pk>/', StudentAppEdit, name='student_application_edit'),
   path('student_application_delete/<int:pk>/', StudentAppDelete, name='student_application_delete'),
   
   path('agent_application_create/', AgentAppCreateBlank, name='agent_application_create2'),
   path('agent_application_create/<int:university_id>/<int:course_id>/', AgentAppCreate, name='agent_application_create'),
   path('agent_application/<int:pk>/', AgentAppDetails, name='agent_application'),
   path('agent_application/<int:pk>/', AgentAppDetails, name='agent_application'),
   path('agent_application_edit/<int:pk>/', AgentAppEdit, name='agent_application_edit'),
   path('agent_application_delete/<int:pk>/', AgentAppDelete, name='agent_application_delete'),
   

   
   
  
]
