from django.contrib import admin
from .models import Service
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name','status')

admin.site.register(Service,ServiceAdmin)



