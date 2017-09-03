from django.conf.urls import url
from resume.views import sendEmail

app_name = 'resume'

urlpatterns = [
    url(r'^ajax/send_email/$', sendEmail, name='send_email'),
]
