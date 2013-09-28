#Python imports
import logging

#Django imports
from django.db import models

#App imports
from .managers import *

logger = logging.getLogger(__name__)

# Create your models here.

class Timestamped(models.Model):
    created  = models.DateTimeField(auto_now_add=True,
                   help_text="Date the model was created.")
    modified = models.DateTimeField(auto_now=True,
                   help_text="Date the model was modified.")
    
    class Meta:
        abstract = True

