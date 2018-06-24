from django.conf.urls import url, include
from django.contrib import admin
from resume import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.AboutMe.as_view(), name='About_Me'),
    url(r'^resume/$', views.Resume.as_view(), name='resume'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^ajax/send_email/$', views.send_email, name='send email'),
    url(r'^[\w]+/', include('resume.urls')),
]
