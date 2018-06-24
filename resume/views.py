from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from resume.forms import ContactForm
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
import json
import requests


base_templte = 'base.html'
about_template = 'resume/AboutMe.html'
resume_template = 'resume/resume.html'
contactMe_template = 'resume/contact.html'
email_auto_replay_template = 'resume/auto_reply_email.html'
email_forwarding_template = 'resume/email_received.html'

class BaseContact(View):
    """
    Base contact view from which all other view with contact lightbox will inherit from.
    """
    def __init__(self, template=base_templte):
        self.template_name = template
        self.contact_form = ContactForm(None)

    @method_decorator(csrf_protect)
    def get(self, request):
        context = {'contact': self.contact_form}
        return render(request, self.template_name, {'contact': self.contact_form})



class AboutMe(BaseContact):
    def __init__(self, template=about_template):
        super().__init__(template=about_template)


class Resume(BaseContact):
    def __init__(self, template=resume_template):
        super().__init__(template=resume_template)



class ContactView(BaseContact):
    def __init__(self, template=contactMe_template):
        super().__init__(template=contactMe_template)


def recaptcha_validation(captcha_token):
    # recaptcha_response = request.POST.get('recaptcha')
    data = {
    'secret': settings.GOOGLE_RECAPTCHA_KEY,
    'response': captcha_token
    }
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)

    return r.json()['success']


def send_mail(email_from, subject, email_template, email_context, to_email=[None]):
    """
    Generic send email method
    :email_from -> email type ex. email@example.com
    :to_email -> list of email one or more
    :subject -> uniline string
    :email_template -> html file path of the email to send
    :email_context -> dictionnary context data to render email_template.
    """
    body = render_to_string(email_template, email_context)
    email_message = EmailMultiAlternatives(subject, body, email_from, to_email)
    if body:
        html_email = render_to_string(email_template, email_context)
        email_message.attach_alternative(html_email, 'text/html')
    email_message.send()


@csrf_protect
def send_email(request):
    if request.is_ajax() and request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        form = ContactForm(recaptcha_response, request.POST)

        if form.is_valid():
            # Autoreply to sender.
            from_email = 'clovis@dnclovis.com'
            to_email = [ form.cleaned_data.get('email') ]
            context = {'name': form.cleaned_data.get('name')}
            subject_autoreply = 'Thank you, ' + context['name'].title() + ' for your message.'
            send_mail(from_email, subject_autoreply, email_auto_replay_template, context, to_email=to_email)

            # Forwarding incoming message.
            context = {'message': form.cleaned_data.get('message').strip(), 'from': to_email[0]}
            subject = form.cleaned_data.get('subject')
            send_mail(from_email, subject, email_forwarding_template, context, to_email=['clovis@dnclovis.com'])

            data = {'status': 'good'}
            return JsonResponse(data, status=200)
        else:
            data = {'status': 'Please verify the fields and try again, thanks!'}
            return JsonResponse(data)
    else:
        return HttpResponseBadRequest('Error: Invalid Request!')
