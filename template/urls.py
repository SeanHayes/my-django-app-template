#Django imports
from django.conf.urls.defaults import *

#App imports
from .views import index

# place app url patterns here
urlpatterns = patterns('',
	url(r'^$', index, name="{{ app_name }}_index"),
)
