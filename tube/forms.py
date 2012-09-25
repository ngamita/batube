from django import forms
from batube.tube.models import Post, Comment


class PostAdminForm(forms.ModelForm):
	class Meta:
		model = Post

	#def clean_story(self):
		# validation happens here.
	#	pass



# Adding the Comment Form Here.
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		exclude = ['post']

