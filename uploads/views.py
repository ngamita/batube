# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


from batube.uploads.models import Document
from batube.uploads.forms import DocumentForm

def list(request):
	# handle file upload
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'])
			newdoc.save()

			# Redirect tp document list after POST
			return HttpResponseRedirect(reverse('uploads.views.list'))
	else:
		form = DocumentForm() #A empty, unbound form


		# Load documents for the list page
	documents = Document.objects.all()


		# Render list page with the documents and the form
	return render_to_response('uploads/list.html', {'documents': documents, 'form': form}, context_instance=RequestContext(request))

