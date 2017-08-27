from django.shortcuts import render
from django.views.generic import View, TemplateView
# Create your views here.

class AboutMe(TemplateView):
    template_name = 'aboutMe/AboutMe.html'
