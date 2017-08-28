from django.shortcuts import render
from django.views.generic import View, TemplateView
# Create your views here.

class AboutMe(TemplateView):
    template_name = 'resume/AboutMe.html'

class Resume(TemplateView):
    template_name = 'resume/resume.html'

class Contact(TemplateView):
    template_name = 'resume/contact.html'
