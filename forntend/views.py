from django.shortcuts import render, redirect
from backend.models import *
from. forms import *
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string
import threading
# Create your views here.


def Home(request):
    return render(request, 'index.html')

def AboutUs(request):
    return render(request, 'about_us.html')

def StudyUK(request):
    return render(request, 'why_in_uk.html')

def ApplicationProcess(request):
    return render(request, 'application_process.html')

def WhyUs(request):
    return render(request, 'why_choose_admission_network.html')

def UkUniversities(request):
    univerities=University.objects.filter(Country='UK')
    context={"univerities":univerities,}
    return render(request, 'uk_universities.html', context)

def StudyUsa(request):
    return render(request, 'why_in_usa.html')

def ApplicationProcessUSA(request):
    return render(request, 'application_process_usa.html')

def USAUniversities(request):
    univerities=University.objects.filter(Country='USA')
    context={"univerities":univerities,}
    return render(request, 'usa_universities.html', context)

def UniversrityDetails(request,pk):
    university=University.objects.get(pk=pk)    
    context={'university':university,}
    return render(request, 'university_details.html', context)

def DetailCourse(request,pk):
    
    course=Course.objects.get(pk=pk)
    
    context={'course':course,}
    return render(request, 'course_details.html', context)

def send_booking_email(user_email, first_name):
    subject = "Admission Network - Registration Complete!"
    from_email = "allan01941@gmail.com"
    html_message = render_to_string('email/booking.html', {'first_name': first_name, 'email':user_email})
    plain_message = strip_tags(html_message)
    email = EmailMultiAlternatives(subject, plain_message, from_email, to=[user_email])
    email.attach_alternative(html_message, "text/html")
    email.send()

def ContactUs(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "We've received your message. One of our executives will contact you shortly.")
            
            # Corrected email_thread parameters
            email_thread = threading.Thread(target=send_booking_email, args=(form.cleaned_data['email'], form.cleaned_data['first_name']))
            email_thread.start()
            
            return redirect('index')
    else:
        form = ContactForm()
    
    return render(request, 'contact_us.html', {'form': form})



