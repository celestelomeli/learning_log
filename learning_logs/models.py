from django.db import models

# Create your models here.

class Topic(models.Model):
	"""A topic the user is learning about."""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		"""Return a string representation of the model."""
		return self.text


class Entry(models.Model):
	"""Something specific learned about a topic."""
	#foreign is reference to another record in database, connects entry to specific topic
	# on_delete means when topic all entries associated should also delete
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	# text of entries
	text = models.TextField()
	# present entries in order created with timestamp
	date_added = models.DateTimeField(auto_now_add=True)

	# holds extra info for managing model; here it specifies to use plural form when referring to mulitple entries
	class Meta:
		verbose_name_plural = 'entries'
		
	# show first 50 characters of text 
	def __str__(self):
		"""Return a string representation of the model."""
		return f"{self.text[:50]}..."
