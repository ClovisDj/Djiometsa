from django.shortcuts import render
from django.views.generic import TemplateView
from resume.models import Contact
from resume.form import ContactModelForm
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
# Create your views here.

class AboutMe(TemplateView):
    template_name = 'resume/AboutMe.html'

class Resume(TemplateView):
    template_name = 'resume/resume.html'

class ContactView(TemplateView):
    template_name = 'resume/contact.html'


# Ajax send Email Handling

def validateEmail(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False


def sendEmail(request):
    if request.is_ajax() and request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            if validateEmail(email):
                if Contact.objects.all().filter(email__iexact=email):
                    currentContact = Contact.objects.get(email__iexact=email)
                    currentContact.subject = subject
                    currentContact.message = message
                    currentContact.save()

                else:
                    currentContact = Contact()
                    currentContact.name = name
                    currentContact.email = email
                    currentContact.subject = subject
                    currentContact.message = message
                    currentContact.save()

                from_email = 'clovis@dnclovis.com'
                html_autoReply = "<p>Dear <strong>"+name.title()+" </strong></p><p>Thank you for reaching me out, I will respond assoon as possible.</p><p>Thank You!</p><br><p>-------</p><p>Clovis Djiometsa</p><p>Full Stack Web Developer</p>"
                subject_autoreply = name+' Thank you for your message.'
                msg = EmailMultiAlternatives(subject_autoreply, html_autoReply, from_email, [email])
                msg.attach_alternative(html_autoReply, "text/html")
                msg.send()
                msg_toMe = EmailMultiAlternatives(subject, 'From: '+email+': '+message, from_email, [from_email])
                msg_toMe.send()

                data = {'status': 'good'}
                return JsonResponse(data)

            else:
                data = {'status': 'Invalid email. Please verify your email and resubmit. thanks!'}
                return JsonResponse(data)
        else:
            data = {'status': 'Please verify the fields and try again, thanks!'}
            return JsonResponse(data)
    else:
        raise Http404
