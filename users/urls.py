"""Defines URL patterns for users"""

from django.urls import path, include

# import views module from users
from . import views

app_name = 'users'
urlpatterns = [
	# Include default auth urls.
	path('', include('django.contrib.auth.urls')),
    # Registration page, sends requests to register function
	path('register/', views.register, name='register'),
]

