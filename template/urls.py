#Django imports
from django.conf.urls.defaults import *

# place app url patterns here
urlpatterns = patterns('some_app.views',
	url(r'^$', 'index', name="some_app_index"),
)
