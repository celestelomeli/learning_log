from django.contrib import admin

# Register your models here.

from .models import Topic, Entry 

# Manage model through admin site
admin.site.register(Topic) 
admin.site.register(Entry)

