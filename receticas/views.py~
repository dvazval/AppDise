from django.contrib.auth.views import login
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from forms import CreateRecetaForm


from models import Receta


def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect()
    else:
        return login(request)

def index(request):
    return render_to_response("rece/index.html",
                              RequestContext(request))

class RecetaDisplayView(DetailView):
	#template_name = "recetas/receta.html"
	
	def get_context_data(self, **kwargs):
		context = super(RecetaDisplayView, self).get_context_data(**kwargs)
		context['receta']= Receta.objects.get(pk=self.kargs.get('receta_id', None))
		return context

class RecetaListView(ListView):
	#template_name = "recetas/receta.html"
	
	def get_context_data(self, **kwargs):
		context = super(RecetaListView, self).get_context_data(**kwargs)
		context['recetas']= Receta.objects
		return context

class RecetaCreate(CreateView):
    template_name = "recetas/recetaCreate.html"
    model = Receta
    #form_class = CreateRecetaForm
    fields = ['idreceta','nombre','tiempo','descripcion']

class RecetaUpdate(UpdateView):
    template_name = "recetas/recetaUpdate.html"
    model = Receta
    fields = ['nombre','tiempo','descripcion']


class RecetaDelete(DeleteView):
    template_name = "recetas/recetaUpdate.html"
    model = Receta
    success_url = reverse_lazy('recetas')

	 
