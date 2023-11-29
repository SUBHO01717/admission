from django.shortcuts import render, redirect
from backend.models import *
from. forms import *
from. models import *
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string
import threading
from backend.decorators import *
# Create your views here.


def Home(request):
    return render(request, 'index.html')

def AboutUs(request):
    return render(request, 'about_us.html')

def Student(request):
    return render(request, 'students.html')
def Recruiter(request):
    return render(request, 'recruitment_partner.html')
def Partner(request):
    return render(request, 'institutional_partner.html')
def TermsConditions(request):
    return render(request, 'terms_conditions.html')
def NewsBlogs(request):
    blogs=BlogNews.objects.all()
    return render(request, 'news_and_blogs.html',{'blogs':blogs} )
def EventAll(request):
    events=Events.objects.all()
    return render(request, 'events.html', {'events':events})

def StudyUK(request):
    return render(request, 'why_in_uk.html')

def ApplicationProcess(request):
    return render(request, 'application_process.html')

def ApplicationProcessLocal(request):
    return render(request, 'application_process_local_UK.html')

def WhyUs(request):
    return render(request, 'why_choose_admission_network.html')

# def UKInstitutions(request ,institution_type=None, Accepted=None):
    
#     if institution_type:
#         universities = University.objects.filter(type=institution_type)
#     if Accepted:
#         universities = University.objects.filter(accept_student=Accepted)
#     else:
#         universities = University.objects.filter(country='UK')
    
#     context={"universities":universities,'institution_type':institution_type, 'Accepted': Accepted}
#     return render(request, 'UK_Institutions.html', context)


def UKInstitutions(request, institution_type=None, Accepted=None):
    universities = University.objects.filter(country='UK')
    print(institution_type)

    if institution_type:
        universities = universities.filter(type=institution_type)

    if Accepted:
        # Filter based on the actual value from the choices
        universities = universities.filter(accept_student=Accepted)

    context = {
        "universities": universities,
        'institution_type': institution_type,
        'Accepted': Accepted,
    }

    return render(request, 'UK_Institutions.html', context)

def UkUniversities(request):
    univerities=University.objects.filter(Country='UK')
    context={"univerities":univerities,}
    return render(request, 'uk_universities.html', context)

def UkUniversities(request):
    univerities=University.objects.filter(Country='UK', type="University")
    context={"univerities":univerities,}
    return render(request, 'uk_universities.html', context)

def UKColleges(request):
    univerities=University.objects.filter(Country='UK', type="College")
    context={"univerities":univerities,}
    return render(request, 'uk_colleges.html', context)

def StudyUsa(request):
    return render(request, 'why_in_usa.html')

def ApplicationProcessUSA(request):
    return render(request, 'application_process_usa.html')

def USAUniversities(request):
    univerities=University.objects.filter(Country='USA', type="University")
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

def send_contact_email(user_email, first_name):
    subject = "Admission Network - Registration Complete!"
    from_email = "allan01941@gmail.com"
    html_message = render_to_string('email/booking.html', {'first_name': first_name, 'email':user_email})
    plain_message = strip_tags(html_message)
    email = EmailMultiAlternatives(subject, plain_message, from_email, to=[user_email])
    email.attach_alternative(html_message, "text/html")
    email.send()

def ContactUs(request):
    office=GlobalOffice.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "We've received your message. One of our executives will contact you shortly.")
            
            # Corrected email_thread parameters
            email_thread = threading.Thread(target=send_contact_email, args=(form.cleaned_data['email'], form.cleaned_data['first_name']))
            email_thread.start()
            
            return redirect('index')
    else:
        form = ContactForm()
    
    return render(request, 'contact_us.html', {'form': form, 'office':office})


def EventCreate(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Event Created Successfully!")
            return redirect('userprofile')
    else:
         form = EventForm()

    return render(request, 'create/event_create.html' , {'form': form})

def BlogNewsCreate(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog Created Successfully!")
            return redirect('userprofile')
    else:
         form = BlogForm()

    return render(request, 'create/blog_and_news_create.html' , {'form': form})


def appointment_email(user_email, course, university, date ):
    subject = "Admission Network - Appointment Booked!"
    from_email = "allan01941@gmail.com"
    html_message = render_to_string('email/booking_.html', {'email': user_email,  'course':course, 'university':university, 'date':date})
    plain_message = strip_tags(html_message)
    email = EmailMultiAlternatives(subject, plain_message, from_email, to=[user_email])
    email.attach_alternative(html_message, "text/html")
    email.send()

def UserBookAppointments(request):
    if request.method == 'POST':
        form = Bookingform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "We've received your message. One of our executives will contact you shortly.")
            
            # Corrected email_thread parameters
            email_thread = threading.Thread(target=appointment_email, args=(form.cleaned_data['email'], form.cleaned_data['course'], form.cleaned_data['university'], form.cleaned_data['date']))
            email_thread.start()
            
            return redirect('index')
    else:
        form = Bookingform()
    
    return render(request, 'book_appointment.html', {'form': form,})