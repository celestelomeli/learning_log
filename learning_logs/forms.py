from django import forms

# import model we're working with
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	# tells django which model to base form on and which fields to include in form
	class Meta:
		# build form from topic model and include only text field 
		model = Topic
		fields = ['text']
		# Do not generate label for text field 
		labels = {'text': ''}

# 
class EntryForm(forms.ModelForm):
	class Meta:
		# model entryform is based on and fields to include
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		# include this to override default widget choices; 80 columns wide vs 40 
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}


