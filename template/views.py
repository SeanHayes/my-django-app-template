#Python imports
import logging

#Django imports
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

#App imports
from forms import *
from models import *

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    pass

