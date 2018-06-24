from django.conf.urls import url
from resume.views import send_email

app_name = 'resume'

# To allow send email on all app pages
urlpatterns = [
    url(r'^ajax/send_email/$', send_email, name='send_email'),
]
