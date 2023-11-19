from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMultiAlternatives

from .models import UserProfile
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.html import strip_tags

from django.template.loader import render_to_string
import threading
# Create your views here.

def send_welcome_email(user_email, user_name):
    subject = "Admission Network - Registration Complete!"
    from_email = "allan01941@gmail.com"
    html_message = render_to_string('email/welcome-mail.html', {'useremail': user_name})
    plain_message = strip_tags(html_message)

    email = EmailMultiAlternatives(subject, plain_message, from_email, to=[user_email])
    email.attach_alternative(html_message, "text/html")
    email.send()

def userSignup(request):
    error = ""
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        userrole = request.POST['userrole']
        p1 = request.POST['pass1']
        p2 = request.POST['pass2']

        if p1 != p2:
            messages.warning(request, 'Password does not match.')
            return redirect('signup')
        elif User.objects.filter(username=email).exists():
            messages.warning(request, 'Email already taken')
            return redirect('signup')
        else:
            try:
                user = User.objects.create_user(username=email, email=email, password=p1)
                UserProfile.objects.create(user=user, userrole=userrole, phone=phone)
                messages.success(request, 'User registered successfully.')

                # Send email in a separate thread
                email_thread = threading.Thread(target=send_welcome_email, args=(user.email,user.email))
                email_thread.start()

                return redirect('login')
            except Exception as e:
                messages.warning(request, 'Something went wrong: {}'.format(str(e)))

    return render(request, 'register.html')
    
    
def UserLogin(request):
    if request.method=='POST' :
       uname = request.POST['email']
       pass1 = request.POST['pass']
       user= authenticate (request,username= uname, password=pass1)
       if user is not None:
            login(request,user)
            messages.info(request, f'You are logged in as "{user.username}"')
            #user_profile = UserProfile.objects.get(user=request.user)
            return redirect('userprofile')
            # if user_profile.userrole== 'Student':
            #     return redirect('student_view')
            # elif user_profile.userrole == 'Agent':  
            #     return redirect('agent_view')
            # elif user_profile.userrole == 'Staff':
            #     return redirect('admin_view')
            #else:
            #    messages.warning(request,'You are not a registered user')
           
       else:
           messages.warning(request,'Given Information is not correct or user not registered!')
           return redirect('login')
    return render(request,"login.html")



def UserLogout(request):
    messages.warning(request, f'You are logged out successfully.')
    logout(request)
    
    return redirect("index")