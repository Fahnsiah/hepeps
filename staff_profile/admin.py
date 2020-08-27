from django.contrib import admin
from .models import Role, Team, Education, Country, Experience, Certifications,Training,Publication,Projects


# Register your models here.

class EducationAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'city', 'country')


admin.site.register(Role)
admin.site.register(Team)
admin.site.register(Country)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience)
admin.site.register(Certifications)
admin.site.register(Training)
admin.site.register(Publication)
admin.site.register(Projects)
