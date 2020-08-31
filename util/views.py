from django.shortcuts import render
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from .models import SendEmailInfo


def email_response(message, recipients):
    email_info = SendEmailInfo.objects.all()[:1].get()
    send_mail(
        email_info.subject,
        message,
        email_info.sender,
        recipients,
        fail_silently=email_info.fail_silently,
    )
