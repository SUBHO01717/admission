from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(University)
admin.site.register(Campus)
admin.site.register(Course)
admin.site.register(Intake)
admin.site.register(Application)
admin.site.register(AgentApplication)

admin.site.register(DegreeLevel)
admin.site.register(EducationArea)

