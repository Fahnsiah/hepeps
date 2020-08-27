from django.contrib import admin
from .models import Team, Role


class TeamAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_active')


admin.site.register(Team, TeamAdmin)
admin.site.register(Role)
