# Copyright 2012 Batube Inc. All Rights Reserved.

"""URLs for the Tube App.

TODO(@ngamita):
"""

__author__ = 'rebellious.ngamita@gmail.com (Richard Ngamita)'

from django.db import models


from django.conf.urls.defaults import patterns, include, url

from django.conf.urls.defaults import *
from batube import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#Testing the /batube view=previe def=home just render_to_response index.html
	(r'^batube/$', 'preview.views.home'),
    # Example:
    # (r'^batube/', include('batube.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
	#connects to tube urls files
	(r'^', include('tube.urls')),
	#TODO: @ngamita make this non-relative for production.
	(r'static/(?P<path>.*)$', 'django.views.static.serve',
		{ 'document_root' : '/home/ngamita/projects/batube/static' }),
)




handler404 = 'batube.views.file_not_found_404'


