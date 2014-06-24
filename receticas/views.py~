from django.contrib.auth.views import login
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from forms import *


from models import Receta, Recetario


def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect()
    else:
        return login(request)

def index(request):
    return render_to_response("rece/index.html",
                              RequestContext(request))


########################################## RECETAS

class RecetaDisplayView(DetailView):
        model=Receta

	def get_context_data(self, **kwargs):
		context = super(RecetaDisplayView, self).get_context_data(**kwargs)
		context['receta']= Receta.objects.get(pk=self.kwargs.get('pk', None))
		context['pasos']= Pasos.objects.get(idreceta=self.kwargs.get('pk', None))
		context['ingredientes']= IngredienteXReceta.objects.get(idreceta=self.kwargs.get('pk', None))
		return context

	def get_queryset(self):
		result = Recetario.objects.filter(pk=self.kwargs.get('pk', None))
        	return result





class RecetaListView(ListView):
	#template_name = "recetas/receta.html"
	
	def get_context_data(self, **kwargs):
		context = super(RecetaListView, self).get_context_data(**kwargs)
		context['recetas']= Receta.objects
		return context

class RecetaCreate(CreateView):
    template_name = "recetas/formGeneral.html"
    model = Receta
    form_class = CreateReceta

    def get_form_kwargs(self):
        kwargs = super(RecetaCreate, self).get_form_kwargs()
        kwargs['recetario'] = self.kwargs.get('pk', None)
        return kwargs
    success_url = reverse_lazy('misreceticas')
    #fields = ['idreceta','nombre','tiempo','descripcion']

class RecetaUpdate(UpdateView):
    template_name = "recetas/formGeneral.html"
    model = Receta
    fields = ['nombre','tiempo','descripcion']
    success_url = reverse_lazy('misreceticas')


class RecetaDelete(DeleteView):
    template_name = "recetas/formGeneral.html"
    model = Receta
    success_url = reverse_lazy('misreceticas')



########################################## RECETARIOS
class RecetarioDisplayView(DetailView):
	#template_name = "recetas/receta.html"
	model=Recetario

	def get_context_data(self, **kwargs):
		context = super(RecetarioDisplayView, self).get_context_data(**kwargs)
		context['recetario']= "Contexto"
		return context

	def get_queryset(self):
		result = Recetario.objects.filter(pk=self.kwargs.get('pk', None))
        	return result

class RecetarioListView(ListView):
	#template_name = "recetas/receta.html"
	
	def get_context_data(self, **kwargs):
		context = super(RecetarioListView, self).get_context_data(**kwargs)
		context['recetarios']= Recetario.objects
		return context

class RecetarioRecetasListView(ListView):
	#template_name = "recetas/receta.html"
	
	def get_context_data(self, **kwargs):
		context = super(RecetarioRecetasListView, self).get_context_data(**kwargs)
		#context['recetarios']= Recetario.objects
		return context

	def get_queryset(self):
		result = Receta.objects.filter(idrecetario=self.kwargs.get('pk', None))
        	return result




class RecetarioCreate(CreateView):
    template_name = "recetas/formGeneral.html"
    model = Recetario
    form_class = CreateRecetario
    

    def get_form_kwargs(self):
        kwargs = super(RecetarioCreate, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    success_url = reverse_lazy('misreceticas')

class RecetarioUpdate(UpdateView):
    template_name = "recetas/formGeneral.html"
    model = Recetario
    fields = ['nombrer','descripcionr']
    success_url = reverse_lazy('misreceticas')



class RecetarioDelete(DeleteView):
    template_name = "recetas/formGeneral.html"
    model = Recetario
    success_url = reverse_lazy('misreceticas')


class MisReceticasListView(ListView):
	#template_name = "recetas/receta.html"
	
	def get_context_data(self, **kwargs):
		context = super(MisReceticasListView, self).get_context_data(**kwargs)
		return context
	def get_queryset(self):
		sessionIdusuario = self.request.user.id
		result = Recetario.objects.filter(idusuario=sessionIdusuario)
        	return result


class RecetarioRecetasUsuarioListView(ListView):
	#template_name = "recetas/receta.html"
	
	def get_context_data(self, **kwargs):
		context = super(RecetarioRecetasUsuarioListView, self).get_context_data(**kwargs)
		#context['recetarios']= Recetario.objects
		return context

	def get_queryset(self):
		result = Receta.objects.filter(idrecetario=self.kwargs.get('pk', None))
        	return result





#################### PASOS
class PasosListView(ListView):
	#template_name = "recetas/receta.html"
	
	def get_context_data(self, **kwargs):
		context = super(PasosListView, self).get_context_data(**kwargs)
		context['receta']= self.kwargs.get('pk', None)
		return context

	def get_queryset(self):
		result = Pasos.objects.filter(idreceta=self.kwargs.get('pk', None))
        	return result

class PasoCreate(CreateView):
    template_name = "recetas/formGeneral.html"
    model = Pasos
    form_class = CreatePaso

    def get_form_kwargs(self):
        kwargs = super(PasoCreate, self).get_form_kwargs()
        kwargs['receta'] = self.kwargs.get('pk', None)
        return kwargs
    success_url = reverse_lazy('misreceticas')
    #fields = ['idreceta','nombre','tiempo','descripcion']

class PasoUpdate(UpdateView):
    template_name = "recetas/formGeneral.html"
    model = Pasos
    fields = ['pasonumero','contenido']
    success_url = reverse_lazy('misreceticas')


class PasoDelete(DeleteView):
    template_name = "recetas/formGeneral.html"
    model = Pasos
    success_url = reverse_lazy('misreceticas')


