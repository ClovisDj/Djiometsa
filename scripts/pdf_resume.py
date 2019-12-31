import os
from django.conf import settings
from django.template.loader import render_to_string
import pdfkit

from resume.views import SkillSet


RESUME_TEMPLATE = 'resume/resume_pdf.html'


def run():
    template = render_to_string(RESUME_TEMPLATE, context={'skills': SkillSet()})
    css_dir = os.path.join(settings.BASE_DIR, 'resume/static/css')
    pdf_resume_dir = os.path.join(settings.BASE_DIR, 'resume/static/resume')

    css = [
        f'{css_dir}/base.css',
        f'{css_dir}/resumePdf.css'
    ]

    pdfkit.from_string(template, f'{pdf_resume_dir}/resume.pdf', css=css)
