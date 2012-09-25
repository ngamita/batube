# Copyright 2012 Batube Inc. All Rights Reserved.

"""Models for the Tube App.

TODO(@ngamita): Fall back to changes in models
"""

__author__ = 'rebellious.ngamita@gmail.com (Richard Ngamita)'

from django.db import models




# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length = 50)
	slug = models.SlugField(max_length = 50, unique=True, help_text = 'Unique value for tube posts page URL, created from name')
	description = models.TextField()
	is_active = models.BooleanField(default = True)
	meta_keywords = models.CharField("Meta Keywords", max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
	meta_description = models.CharField("Meta Description", max_length=255, help_text='Content for description meta tag')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'categories'
		ordering = ['-created_at']
		verbose_name_plural = 'Categories'

	def __unicode__(self):
		return self.name

	@models.permalink
	def get_absolute_url(self):
		return ('tube_category', (), { 'category_slug': self.slug })

class Post(models.Model):
	title = models.CharField(max_length = 225, unique = True)
	slug = models.SlugField(max_length = 225, unique = True,
			help_text = 'Unique value for post page URL, created from title')
	tube = models.URLField(max_length = 200, null=True, blank=True)
	story = models.TextField()
	is_published = models.BooleanField(default = False)
	meta_keywords = models.CharField(max_length = 255, help_text = 'Comma-delimited set of SEO keywords')
	meta_description = models.CharField(max_length = 255, help_text='Content for description meta tag')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	categories = models.ManyToManyField(Category)


	class Meta: 
		db_table = 'posts'
		ordering = ['-created_at']
	
	def __unicode__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ('tube_post', (), { 'post_slug': self.slug })


class Comment(models.Model):
	name = models.CharField(max_length = 45)
	email = models.EmailField(max_length = 75)
	text = models.TextField()
	post = models.ForeignKey(Post)
	created_at = models.DateTimeField(auto_now_add = True)


	def __unicode__(self):
		return self.text
