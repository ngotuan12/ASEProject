'''
Created on Apr 3, 2014

@author: TuanNA
'''
import os

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from myapp.forms import DocumentForm
from myapp.models.Documents import Documents


@login_required(login_url='/signin')
def index(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		# Redirect to the document list after POST
		if form.is_valid():
			handle_uploaded_file(request.user,request.FILES['docfile'])
		return HttpResponseRedirect("")
	else:
		form = DocumentForm() # A empty, unbound form
	# Load documents for the list page
	documents = Documents.objects.all()     
	# Render list page with the documents and the form
	return render_to_response(
'myapp/documents.html',
{'documents': documents, 'form': form},
context_instance=RequestContext(request)
)
def handle_uploaded_file(user,f):
	folder_path = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__),os.pardir),os.pardir))+"/common/upload/"+user.username+"/";
	if os.path.isdir(folder_path) == False:
		os.makedirs(folder_path)
	with open(os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__),os.pardir),os.pardir))+"/common/upload/"+user.username+"/"+f.name, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)