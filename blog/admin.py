from django.contrib import admin
from .models import BlogCategory, Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date')


admin.site.register(BlogCategory)
admin.site.register(Blog, BlogAdmin)
