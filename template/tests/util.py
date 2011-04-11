#Django imports
from django.contrib.auth.models import User
from django.test import TestCase

class BaseTestCase(TestCase):
	def setUp(self):
		self.username = 'test_user'
		self.password = 'foobar'
		self.user = User.objects.create_user(self.username, 'test_user@example.com', self.password)\
		
		self.client.login(username=self.username, password=self.password)
	
