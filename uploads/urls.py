from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('uploads.views', 
		(r'^list/$', 'list', name='list'),
		)
