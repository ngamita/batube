# Create your views here.
from django.shortcuts import redirect, get_object_or_404, render_to_response
from batube.tube.models import Category, Post, Comment
from django.template import RequestContext

from models import Post
from forms import CommentForm



def index(request, template_name="tube/index.html"):
	page_title = 'Funny, Dumb Ugandan Videos'
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def show_category(request, category_slug, template_name="tube/category.html"):
	c = get_object_or_404(Category, slug=category_slug)
	posts = c.post_set.all()
	page_title = c.name
	meta_keywords = c.meta_keywords
	meta_description = c.meta_description
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def show_post(request, post_slug, template_name="tube/post.html"):
	p = get_object_or_404(Post, slug=post_slug)
	categories = p.categories.filter(is_active = True)
	page_title = p.title
	meta_keywords = p.meta_keywords
	meta_description = p.meta_description
	# Note comment form as comment_form. Don't confuse this.
	comment_form = CommentForm(request.POST or None)
	if comment_form.is_valid():
		comment = comment_form.save(commit = False)
		comment.post = p
		comment.save()
		# Adding user sessions so that they don't fill in details always.
		request.session["name"] = comment.name
		request.session['email'] = comment.email
		return redirect(request.path)
	comment_form.initial['name'] = request.session.get('name')
	comment_form.initial['email'] = request.session.get('email')
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))

