from django.db import models
from django_mysql.models import ListCharField, JSONField
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    subject = models.CharField(max_length=150)
    message = models.CharField(max_length=1000)
    count = models.IntegerField()
    messageList = ListCharField(
        base_field=models.CharField(max_length=1100),
        max_length=3000,
        default ='',
    )

    def __str__(self):
        return self.name +': '+self.email
