from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.shortcuts import render

def index( request ):
  page = _("You're in home") 
  
  view_param = {
    "page": page
  }
  return render(request, 'index.html', view_param)

def about(request):
  return HttpResponse( _("About my website") )