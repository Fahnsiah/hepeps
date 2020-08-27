from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: "
                                     "'+999999999'. Up to 15 digits allowed.")


class SendEmailInfo(models.Model):
    subject = models.CharField(max_length=150)
    sender = models.CharField(max_length=100)
    fail_silently = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)
