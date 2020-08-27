from django.contrib import admin
from .models import Contact, ContactMessage

admin.site.register(ContactMessage)
admin.site.register(Contact)


