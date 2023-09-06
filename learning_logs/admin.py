from django.contrib import admin

# Register your models here.

from .models import Topic

# Manage model through admin site
admin.site.register(Topic) 
