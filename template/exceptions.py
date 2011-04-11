#Python imports
import logging

logger = logging.getLogger(__name__)

# place exception definitions here

class Error(Exception):
	"""Base class for exceptions in this module."""
	def __str__(self):
		return self.msg

