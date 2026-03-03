from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Topic, Entry


class TopicModelTest(TestCase):
	"""Test the Topic model"""
	
	def setUp(self):
		self.user = User.objects.create_user(username='testuser', password='testpass123')
		self.topic = Topic.objects.create(text='Python Basics', owner=self.user)
	
	def test_topic_creation(self):
		"""Test that a topic is created correctly"""
		self.assertEqual(self.topic.text, 'Python Basics')
		self.assertEqual(self.topic.owner, self.user)
		self.assertIsNotNone(self.topic.date_added)
	
	def test_topic_str_representation(self):
		"""Test the string representation of a topic"""
		self.assertEqual(str(self.topic), 'Python Basics')


class EntryModelTest(TestCase):
	"""Test the Entry model"""
	
	def setUp(self):
		self.user = User.objects.create_user(username='testuser', password='testpass123')
		self.topic = Topic.objects.create(text='Django', owner=self.user)
		self.entry = Entry.objects.create(
			topic=self.topic,
			text='Django is a high-level Python web framework that encourages rapid development.'
		)
	
	def test_entry_creation(self):
		"""Test that an entry is created correctly"""
		self.assertEqual(self.entry.topic, self.topic)
		self.assertIn('Django is a high-level', self.entry.text)
		self.assertIsNotNone(self.entry.date_added)
	
	def test_entry_str_truncation(self):
		"""Test that entry string representation is truncated to 50 chars"""
		self.assertEqual(len(str(self.entry)), 53)  # 50 chars + "..."


class TopicViewAuthorizationTest(TestCase):
	"""Test authorization for topic views"""
	
	def setUp(self):
		self.client = Client()
		self.user1 = User.objects.create_user(username='alice', password='alice123')
		self.user2 = User.objects.create_user(username='bob', password='bob123')
		self.topic = Topic.objects.create(text='Alice Topic', owner=self.user1)
	
	def test_topic_view_requires_login(self):
		"""Test that viewing a topic requires login"""
		response = self.client.get(reverse('learning_logs:topic', args=[self.topic.id]))
		self.assertEqual(response.status_code, 302)  # Redirect to login
		self.assertIn('/users/login/', response.url)
	
	def test_user_cannot_view_others_topic(self):
		"""Test that Bob cannot view Alice's topic"""
		self.client.login(username='bob', password='bob123')
		response = self.client.get(reverse('learning_logs:topic', args=[self.topic.id]))
		self.assertEqual(response.status_code, 404)
	
	def test_user_can_view_own_topic(self):
		"""Test that Alice can view her own topic"""
		self.client.login(username='alice', password='alice123')
		response = self.client.get(reverse('learning_logs:topic', args=[self.topic.id]))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Alice Topic')


class EntryViewAuthorizationTest(TestCase):
	"""Test authorization for entry views"""
	
	def setUp(self):
		self.client = Client()
		self.user1 = User.objects.create_user(username='alice', password='alice123')
		self.user2 = User.objects.create_user(username='bob', password='bob123')
		self.topic = Topic.objects.create(text='Alice Topic', owner=self.user1)
		self.entry = Entry.objects.create(topic=self.topic, text='Alice entry content')
	
	def test_user_cannot_add_entry_to_others_topic(self):
		"""Test that Bob cannot add an entry to Alice's topic"""
		self.client.login(username='bob', password='bob123')
		response = self.client.get(reverse('learning_logs:new_entry', args=[self.topic.id]))
		self.assertEqual(response.status_code, 404)
	
	def test_user_can_add_entry_to_own_topic(self):
		"""Test that Alice can add an entry to her own topic"""
		self.client.login(username='alice', password='alice123')
		response = self.client.get(reverse('learning_logs:new_entry', args=[self.topic.id]))
		self.assertEqual(response.status_code, 200)
	
	def test_user_cannot_edit_others_entry(self):
		"""Test that Bob cannot edit Alice's entry"""
		self.client.login(username='bob', password='bob123')
		response = self.client.get(reverse('learning_logs:edit_entry', args=[self.entry.id]))
		self.assertEqual(response.status_code, 404)
	
	def test_user_can_edit_own_entry(self):
		"""Test that Alice can edit her own entry"""
		self.client.login(username='alice', password='alice123')
		response = self.client.get(reverse('learning_logs:edit_entry', args=[self.entry.id]))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Alice entry content')


class NewTopicViewTest(TestCase):
	"""Test the new_topic view"""
	
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user(username='alice', password='alice123')
		self.client.login(username='alice', password='alice123')
	
	def test_new_topic_redirects_after_post(self):
		"""Test that creating a new topic redirects to topics page"""
		response = self.client.post(
			reverse('learning_logs:new_topic'),
			{'text': 'New Topic'}
		)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, reverse('learning_logs:topics'))
	
	def test_new_topic_creates_topic(self):
		"""Test that posting to new_topic actually creates a topic"""
		initial_count = Topic.objects.count()
		self.client.post(
			reverse('learning_logs:new_topic'),
			{'text': 'Another Topic'}
		)
		self.assertEqual(Topic.objects.count(), initial_count + 1)
		new_topic = Topic.objects.latest('date_added')
		self.assertEqual(new_topic.text, 'Another Topic')
		self.assertEqual(new_topic.owner, self.user)
