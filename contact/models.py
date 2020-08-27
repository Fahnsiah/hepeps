from django.db import models
from util.models import phone_regex


class Contact(models.Model):
    office_phone = models.CharField(max_length=15)
    mobile_phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    website = models.CharField(max_length=100)
    postal = models.TextField()
    photo_url = models.FileField(upload_to='contact', blank=True, null=True)
    publish = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(validators=[phone_regex], max_length=15)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    response = models.TextField()
    has_responded = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


