"""Defines URL patterns for learning_logs."""

from django.urls import path 

# contains view functions: handling HTTP requests, processing data, generating HTTP responses
from . import views 

# helps distinguish file from files with same name in other apps within project 
app_name = "learning_logs"

# Each path maps a URL to a view function and assigns it a name for use in templates
urlpatterns = [ 
	# Home page
	path('', views.index, name='index'),
	# Page that shows all topics 
	path('topics/', views.topics, name='topics'),
	# Detail page for a single topic.
	path('topics/<int:topic_id>/', views.topic, name='topic'),
	# Page for adding a new topic
	path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding new entry 
	# id is number matching topic ID
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
]

