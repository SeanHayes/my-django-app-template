#Django imports
from django.test import TestCase

#App imports
from test_managers import *
from test_models import *
from test_urls import *

__test__ = {
	'test_managers': [test_managers],
	'test_models': [test_models],
	'test_urls': [test_urls],
}

class DefaultTestCase(TestCase):
	def test_foo(self):
		"Just a reminder to write tests for this app. Can be deleted."
		assert False
