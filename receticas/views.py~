from django.contrib.auth.views import login
from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect()
    else:
        return login(request)

def index(request):
    return render_to_response("rece/index.html",
                              RequestContext(request))

