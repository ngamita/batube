from django.contrib import admin
from batube.tube.models import Category, Post, Comment
from batube.tube.forms import PostAdminForm


class PostAdmin(admin.ModelAdmin):
	form = PostAdminForm

	#sets values for how the admin site lists the posts
	list_display = ('title', 'tube', 'story', 'is_published', 'created_at', 'updated_at', )
	list_display_links = ('title', )
	list_per_page = 50
	ordering = ['-created_at']
	search_fields = ['title', 'story', 'meta_keywords', 'meta_description']
	#exclude = ('created_at', 'updated_at', )

	#sets up slug to be generated from the posts title
	prepopulated_fields = {'slug': ('title', )}
	readonly_fields = ('created_at', 'updated_at',)

# registers the posts model with the admin site
admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
	# sets up the values for how admin site lists categories
	list_display = ('name', 'created_at', 'updated_at', )
	list_display_links = ('name', )
	list_per_page = 20
	ordering = ['name']
	search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
	#exclude = ('created_at', 'updated_at', )
	readonly_fields = ('created_at', 'updated_at',)


	#sets up slug to be generated from category name
	prepopulated_fields = { 'slug' : ('name', ) }

admin.site.register(Category, CategoryAdmin)
	

