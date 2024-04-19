from django.db import models
from django import forms
from django.contrib.auth.models import User
from core.models import Unidade


# class CustomUser(models.Model):
#     user = models.OneToOneField(User, related_name='custom_user')
#     unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT)


class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"


class DateTimeLocalField(forms.DateTimeField):
    input_formats = [
        "%Y-%m-%dT%H:%M:%S", 
        "%Y-%m-%dT%H:%M:%S.%f", 
        "%Y-%m-%dT%H:%M",
    ]
    widget = DateTimeLocalInput(format="%Y-%m-%dT%H:%M")
