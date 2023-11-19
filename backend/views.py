from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count,Sum
from . models import *
from accounts.models import *
from .forms import *
from django.views import generic
from django.contrib import messages
from . decorators import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
@role_required(allowed_roles=["Staff","Agent","Student","Partner"])
def Profile(request):
    university=University.objects.all()
    course=Course.objects.all()
    intake=Intake.objects.all()
    campus=Campus.objects.all()
    student = User.objects.filter(userprofile__userrole="Student")
    partner = User.objects.filter(userprofile__userrole="Partner")
    agent = User.objects.filter(userprofile__userrole="Agent")
    agentapplication = AgentApplication.objects.all()
    application = Application.objects.all()
    
    
    particular_agent_application = AgentApplication.objects.filter(applicant=request.user)
    agent_application_accepted = AgentApplication.objects.filter(applicant=request.user, application_status='Approved')
    agent_application_pending = AgentApplication.objects.filter(applicant=request.user, application_status='Pending')
    agent_application_onprocess = AgentApplication.objects.filter(applicant=request.user, application_status='On Process')
    agent_application_rejected = AgentApplication.objects.filter(applicant=request.user, application_status='Rejected')
    agent_application_returned = AgentApplication.objects.filter(applicant=request.user, application_status='Returned')
    
    particular_student_application = Application.objects.filter(applicant=request.user)
    student_application_accepted = Application.objects.filter(applicant=request.user, application_status='Approved')
    student_application_pending = Application.objects.filter(applicant=request.user, application_status='Pending')
    student_application_onprocess = Application.objects.filter(applicant=request.user, application_status='On Process')
    student_application_rejected = Application.objects.filter(applicant=request.user, application_status='Rejected')
    student_application_returned = Application.objects.filter(applicant=request.user, application_status='Returned')
    
       
    status_counts = AgentApplication.objects.values('application_status').annotate(status_count=Count('application_status'))
    status_counts_student = Application.objects.values('application_status').annotate(status_count=Count('application_status'))
    
    
    # For Partner Profile
    partner_profile = request.user.userprofile

    universities_with_counts = University.objects.filter(partners=partner_profile).annotate(
        agent_application_count=Count('agentapplication'),
        student_application_count=Count('application')
    )
    
    universities_with_course_count = University.objects.filter(partners=partner_profile).annotate(
    course_count=Count('course'))

# Calculate the total counts for agent and student applications across all universities
    partner_total = universities_with_counts.aggregate(
        total_agent_applications=Sum('agent_application_count'),
        total_student_applications=Sum('student_application_count')
    )

# Access the total counts
    total_agent_applications = partner_total['total_agent_applications']
    total_student_applications = partner_total['total_student_applications']
    
    partner_total=(total_agent_applications or 0 )+(total_student_applications or 0)
    
    context={
        'university':university,
        'course':course,
        'intake':intake,
        'campus':campus,
        'student':student,
        'partner':partner,
        'agent':agent,
        'agentapplication':agentapplication,
        'application':application,
        'status_counts':status_counts,
        'status_counts_student':status_counts_student,
        'particular_agent_application':particular_agent_application,
        'agent_application_accepted':agent_application_accepted,
        'agent_application_pending':agent_application_pending,
        'agent_application_onprocess':agent_application_onprocess,
        'agent_application_rejected':agent_application_rejected,
        'agent_application_returned':agent_application_returned,
        
        'particular_student_application':particular_student_application,
        'student_application_accepted':student_application_accepted,
        'student_application_pending':student_application_pending,
        'student_application_onprocess':student_application_onprocess,
        'student_application_rejected':student_application_rejected,
        'student_application_returned':student_application_returned, 
        
        'partner_total':partner_total,
        'universities_with_course_count':universities_with_course_count            
        }
    return render(request,"profile.html", context)


def UniversityDetails(request,pk):
    data=get_object_or_404(University, pk=pk)
    #data = University.objects.get(pk=pk)
    campuses = data.campus_set.all()
    courses = data.course_set.all() 
    context={'data':data, 'campuses':campuses, 'courses':courses,}
    return render(request,"details/unidetail.html", context)

def CourseDetails(request,pk):
   
    data = Course.objects.get(pk=pk)
    context={'data':data, }
    return render(request,"details/coursedetail.html", context)

@login_required(login_url="login")
@role_required(allowed_roles=["Staff"])
def AgentEdit(request,pk):
    user=get_object_or_404(User, pk=pk)
    #user=User.objects.get(pk=pk)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('userprofile')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=user.userprofile)

    return render(request,"edits/agentedit.html", {'user_form': user_form, 'profile_form': profile_form})

@login_required(login_url="login")
@role_required(allowed_roles=["Staff"])
def StudentEdit(request,pk):
    user=User.objects.get(pk=pk)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('userprofile')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=user.userprofile)

    return render(request,"edits/studentedit.html", {'user_form': user_form, 'profile_form': profile_form})

@login_required(login_url="login")
@role_required(allowed_roles=["Staff"])
def DeleteProfile(request, pk):
    data=User.objects.get(pk=pk)
    if request.method == 'POST':
        data.delete()
        messages.warning(request, ' Selected Agent Deleted Successfully!')
        return redirect('userprofile')
    else:
        return render(request,"deletes/deleteprofile.html", {"data":data,}) 

@login_required(login_url="login")
@role_required(allowed_roles=["Staff"])
def CreateUniversity(request):
    if request.method == 'POST':
        uni_form = UniversityForm(request.POST,)
        if uni_form.is_valid():
            uni_form.save()
            messages.success(request, 'Course Data is updated successfully')
            return redirect('userprofile')
    else:
        uni_form = UniversityForm()
    return render(request,"create/create_university.html", {'uni_form': uni_form,}) 

    
@login_required(login_url="login")
@role_required(allowed_roles=["Staff"])
def EditUniversity(request,pk):
    universrity=University.objects.get(pk=pk)
    if request.method == 'POST':
        uni_form = UniversityForm(request.POST,instance=universrity)
        if uni_form.is_valid():
            uni_form.save()
            messages.success(request, 'Info updated successfully')
            return redirect('userprofile')
    else:
        uni_form = UniversityForm(instance=universrity)
    return render(request,"create/create_university.html", {'uni_form': uni_form,}) 


@login_required(login_url="login")
@role_required(allowed_roles=["Staff"])
def CreateCampus(request):
    if request.method == 'POST':
        campus_form = CampusForm(request.POST,)
        if campus_form.is_valid():
            campus_form.save()
            messages.success(request, 'Course Data is updated successfully')
            return redirect('userprofile')
    else:
        campus_form = CampusForm()
    return render(request,"create/create_campus.html", {'campus_form': campus_form,}) 

@login_required(login_url="login")
@role_required(allowed_roles=["Staff"])
def EditCampus(request,pk):
    campus=Campus.objects.get(pk=pk)
    if request.method == 'POST':
        campus_form = CampusForm(request.POST,instance=campus)
        if campus_form.is_valid():
            campus_form.save()
            messages.success(request, 'Info updated successfully')
            return redirect('userprofile')
    else:
        campus_form = CampusForm(instance=campus)
    return render(request,"create/create_campus.html", {'campus_form': campus_form,})

@login_required(login_url="login")
@role_required(allowed_roles=["Staff"])
def CreateCourse(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST,)
        if course_form.is_valid():
            course_form.save()
            messages.success(request, 'Course Data is updated successfully')
            return redirect('userprofile')
    else:
        course_form = CourseForm()
    return render(request,"create/create_course.html", {'course_form': course_form,}) 

@login_required(login_url="login")
@role_required(allowed_roles=["Staff"])
def CourseEdit(request,pk):
    course=Course.objects.get(pk=pk)
    if request.method == 'POST':
        course_form = CourseForm(request.POST, instance=course)
        if course_form.is_valid():
            course_form.save()
            messages.success(request, 'Course Data is updated successfully')
            return redirect('userprofile')
    else:
        course_form = CourseForm(instance=course)
    return render(request,"edits/course-edit.html", {'course_form': course_form,})

@login_required(login_url="login")
@role_required(allowed_roles=["Staff"])
def DeleteCourse(request, pk):
    data=Course.objects.get(pk=pk)
    if request.method == 'POST':
        data.delete()
        messages.warning(request, ' Selected Course Deleted Successfully!')
        return redirect('userprofile')
    else:
        return render(request,"deletes/delete_course.html", {"data":data,}) 
    
@login_required(login_url="login")
@role_required(allowed_roles=["Staff", "Student", "Partner"])
def StudentAppDetails(request,pk):
    application=Application.objects.get(pk=pk)
    context={'application':application,}
    return render(request,"details/student_application_details.html", context)

@login_required(login_url="login")
@role_required(allowed_roles=["Staff", "Student"])
def StudentApplicationCreate(request,university_id,course_id):
    university=University.objects.get(pk=university_id)
    course=Course.objects.get(pk=course_id)
    
    if request.method == 'POST':
        Student_application_form = StudentAppForm2(request.POST)
        if Student_application_form.is_valid():
            Student_application_form.instance.applicant = request.user 
            Student_application_form.save()
            messages.success(request, 'Applciation Created successfully')
            return redirect('userprofile')
    else:
        initial={'university': university, 'course': course}
        Student_application_form = StudentAppForm2(initial=initial)
        
    return render(request,"create/create_student_application.html", {'StudentAppForm': Student_application_form, 'university':university,'course':course })


@login_required(login_url="login")
@role_required(allowed_roles=["Staff", "Student"])
def StudentApplicationCreateBlank(request,):
       
    if request.method == 'POST':
        Student_application_form = StudentAppForm2(request.POST)
        if Student_application_form.is_valid():
            Student_application_form.instance.applicant = request.user 
            Student_application_form.save()
            messages.success(request, 'Applciation Created successfully')
            return redirect('userprofile')
    else:
        Student_application_form = StudentAppForm2()
    return render(request,"create/create_student_application.html", {'StudentAppForm': Student_application_form,})


@login_required(login_url="login")
@role_required(allowed_roles=["Staff"])
def StudentAppEdit(request,pk):
    application=Application.objects.get(pk=pk)
    if request.method == 'POST':
        Student_application_form = StudentAppForm(request.POST, instance=application)
        if Student_application_form.is_valid():
            Student_application_form.save()
            messages.success(request, 'Applciation updated successfully')
            return redirect('userprofile')
    else:
        Student_application_form = StudentAppForm(instance=application)
    return render(request,"edits/student_application_edit.html", {'StudentAppForm': Student_application_form,'application':application})

@login_required(login_url="login")
@role_required(allowed_roles=["Staff"])
def StudentAppDelete(request,pk):
    application=Application.objects.get(pk=pk)
    if request.method == 'POST':
        application.delete()
        messages.warning(request, ' Selected Application Deleted Successfully!')
        return redirect('userprofile')
    else:
        return render(request,"deletes/student_application_delete.html", {"application":application,}) 
    
@login_required(login_url="login")
@role_required(allowed_roles=["Staff", "Agent"])
def AgentAppCreate(request,university_id,course_id):
    university=University.objects.get(pk=university_id)
    course=Course.objects.get(pk=course_id)
    if request.method == 'POST':
        agent_application_form = AgentAppForm2(request.POST)
        if agent_application_form.is_valid():
            agent_application_form.instance.applicant = request.user 
            agent_application_form.save()
            messages.success(request, 'Applciation updated successfully')
            return redirect('userprofile')
    else:
        initial={'university': university, 'course': course}
        agent_application_form = AgentAppForm2(initial=initial)
       
    return render(request,"create/create_agent_application.html", {'AgentAppForm': agent_application_form, 'university':university,'course':course})

@login_required(login_url="login")
@role_required(allowed_roles=["Staff", "Agent"])
def AgentAppCreateBlank(request,):
    if request.method == 'POST':
        agent_application_form = AgentAppForm2(request.POST)
        if agent_application_form.is_valid():
            agent_application_form.instance.applicant = request.user 
            agent_application_form.save()
            messages.success(request, 'Applciation updated successfully')
            return redirect('userprofile')
    else:
        agent_application_form = AgentAppForm2()
    return render(request,"create/create_agent_application.html", {'AgentAppForm': agent_application_form,})


@login_required(login_url="login")
@role_required(allowed_roles=["Staff", "Agent", "Partner"])
def AgentAppDetails(request,pk):
    application=AgentApplication.objects.get(pk=pk)
    context={'application':application,}
    return render(request,"details/agent_application_details.html", context)

@login_required(login_url="login")
@role_required(allowed_roles=["Staff"])
def AgentAppEdit(request,pk):
    application=AgentApplication.objects.get(pk=pk)
    if request.method == 'POST':
        agent_application_form = AgentAppForm(request.POST, instance=application)
        if agent_application_form.is_valid():
            agent_application_form.save()
            messages.success(request, 'Applciation updated successfully')
            return redirect('userprofile')
    else:
        agent_application_form = AgentAppForm(instance=application)
    return render(request,"edits/agent_application_edit.html", {'AgentAppForm': agent_application_form,'application':application})

@login_required(login_url="login")
@role_required(allowed_roles=["Staff"])
def AgentAppDelete(request,pk):
    application=AgentApplication.objects.get(pk=pk)
    if request.method == 'POST':
        application.delete()
        messages.warning(request, ' Selected Application Deleted Successfully!')
        return redirect('userprofile')
    else:
        return render(request,"deletes/student_application_delete.html", {"application":application,}) 

@login_required(login_url="login")
def ProfileEdit(request):
    user=get_object_or_404(User, pk=request.user.id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('userprofile')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=user.userprofile)

    return render(request,"edits/studentedit.html", {'user_form': user_form, 'profile_form': profile_form})

@login_required(login_url="login")
@role_required(allowed_roles=["Staff"])
def PartnerEdit(request,pk):
    user=get_object_or_404(User, pk=pk)
    #user=User.objects.get(pk=pk)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('userprofile')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=user.userprofile)

    return render(request,"edits/partner_edit.html", {'user_form': user_form, 'profile_form': profile_form})