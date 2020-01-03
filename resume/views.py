from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from resume.forms import ContactForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect


BASE_TEMPLATE = 'base.html'
ABOUT_TEMPLATE = 'resume/AboutMe.html'
RESUME_TEMPLATE = 'resume/resume.html'
CONTACT_ME_TEMPLATE = 'resume/contact.html'
EMAIL_AUTO_REPLAY_TEMPLATE = 'resume/auto_reply_email.html'
EMAIL_FORWARDING_TEMPLATE = 'resume/email_received.html'


class SkillSet:
    _instance = None

    class _Skills:
        def __init__(self):
            self.skills_set = ('Python', 'TypeScript', 'Ruby', 'Javascript', 'Html', 'Css',
                               'Jquery', 'Django', 'Django Rest Framework', 'NodeJs', 'AngularJs',
                               'RESTful', 'OpenApi', 'PostgreSql', 'MySql', 'MongoDB', 'Git',
                               'GitHub', 'CircleCi', 'CI/CD', 'Jira', 'Aws', 'Ubuntu', 'Docker', )

            self.mobile_skills = self.get_chunks(self.skills_set, 3)
            self.desktop_skills = self.get_chunks(self.skills_set, 4)

        def get_chunks(self, skills, size):
            to_chunks = []
            for i in range(0, len(skills), size):
                to_chunks.append(skills[i:i + size])
            return to_chunks

    def __new__(cls):
        if not cls._instance:
            cls._instance = cls._Skills()
        return cls._instance


class BaseContact(TemplateView):
    """
    Base contact view from which all other view with contact lightbox will inherit from.
    """
    template_name = BASE_TEMPLATE

    @method_decorator(csrf_protect)
    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            self.get_context_data(contact=ContactForm(), recaptcha=settings.GOOGLE_RECAPTCHA_HTML, resume=False)
        )


class AboutMe(BaseContact):
    template_name = ABOUT_TEMPLATE


class Resume(BaseContact):
    template_name = RESUME_TEMPLATE
    extra_context = {'resume': True, 'skills': SkillSet()}


class ContactView(BaseContact):
    template_name = CONTACT_ME_TEMPLATE


def send_email_message(email_from, subject, email_template, email_context, to_email=None):
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
            to_email = [form.cleaned_data.get('email'), ]
            context = {'name': form.cleaned_data.get('name')}
            subject_autoreply = 'Thank you, ' + context['name'].title() + ' for your message.'
            send_email_message(from_email, subject_autoreply, EMAIL_AUTO_REPLAY_TEMPLATE, context, to_email=to_email)

            # Forwarding incoming message.
            context = {'message': form.cleaned_data.get('message').strip(), 'from': to_email[0]}
            subject = form.cleaned_data.get('subject')
            send_email_message(from_email, subject, EMAIL_FORWARDING_TEMPLATE, context,
                               to_email=['clovis@dnclovis.com', ])

            data = {'status': 'good'}
            return JsonResponse(data, status=200)
        else:
            data = {'status': 'Please verify the fields and try again, thanks!'}
            return JsonResponse(data)

    return HttpResponseBadRequest('Error: Invalid Request!')
