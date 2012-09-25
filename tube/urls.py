from django.conf.urls.defaults import *


urlpatterns = patterns('batube.tube.views',
		(r'^$', 'index', { 'template_name': 'tube/index.html' }, 'tube_home'),
		(r'^category/(?P<category_slug>[-\w]+)/$', 'show_category', { 'template_name': 'tube/category.html' }, 'tube_category'),
		(r'^post/(?P<post_slug>[-\w]+)/$', 'show_post', { 'template_name':'tube/post.html' }, 'tube_post'),		
		
		)
