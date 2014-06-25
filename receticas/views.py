from django.contrib.auth.views import login
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from forms import *
from django.contrib.auth.decorators import login_required



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


###Clase para el view que muestra una receta especifica

class RecetaDisplayView(DetailView):
        model=Receta

	def get_context_data(self, **kwargs):
		context = super(RecetaDisplayView, self).get_context_data(**kwargs)
		### Se obtienen los datos desde la base de datos
		context['receta']= Receta.objects.get(pk=self.kwargs.get('pk', None))
		context['pasos']= Pasos.objects.filter(idreceta=self.kwargs.get('pk', None)).order_by('pasonumero')
		context['ingredientes']= IngredienteXReceta.objects.select_related().filter(idreceta=self.kwargs.get('pk', None))
                #IngredienteXReceta.objects.filter(idreceta=self.kwargs.get('pk', None))
		return context

	def get_queryset(self):
		result = Receta.objects.filter(pk=self.kwargs.get('pk', None))
        	return result

###Clase para el view que muestra todas las recetas de lector

class RecetaListView(ListView):
	
	#Override para definir el contexto
	def get_context_data(self, **kwargs):
		context = super(RecetaListView, self).get_context_data(**kwargs)
		context['recetas']= Receta.objects
		return context

### Clase para la creacion de una receta

class RecetaCreate(CreateView):
    template_name = "recetas/formGeneral.html"
    model = Receta
    form_class = CreateReceta

    def get_form_kwargs(self):
        kwargs = super(RecetaCreate, self).get_form_kwargs()
        kwargs['recetario'] = self.kwargs.get('pk', None)
        return kwargs
     
    success_url = reverse_lazy('misreceticas')

### Clase para el update de una receta

class RecetaUpdate(UpdateView):
    template_name = "recetas/formGeneral.html"
    model = Receta
    fields = ['nombre','tiempo','descripcion']
    success_url = reverse_lazy('misreceticas')

### Clase para borrar una receta

class RecetaDelete(DeleteView):
    template_name = "recetas/formGeneral.html"
    model = Receta
    success_url = reverse_lazy('misreceticas')

########################################## RECETARIOS


## Clase para mostrar la vista detallada de un Recetario

class RecetarioDisplayView(DetailView):
	model=Recetario

	def get_context_data(self, **kwargs):
		context = super(RecetarioDisplayView, self).get_context_data(**kwargs)
		context['recetario']= "Contexto"
		return context

	def get_queryset(self):
		result = Recetario.objects.filter(pk=self.kwargs.get('pk', None))
        	return result

## Vista detallada de un recetario

class RecetarioListView(ListView):
	
	def get_context_data(self, **kwargs):
		context = super(RecetarioListView, self).get_context_data(**kwargs)
		context['recetarios']= Recetario.objects
		return context

## Vista de las recetas de un recetario 

class RecetarioRecetasListView(ListView):
	
	def get_context_data(self, **kwargs):
		context = super(RecetarioRecetasListView, self).get_context_data(**kwargs)
		return context

	def get_queryset(self):
		result = Receta.objects.filter(idrecetario=self.kwargs.get('pk', None))
        	return result


## Clase para crear un recetario

class RecetarioCreate(CreateView):
    template_name = "recetas/formGeneral.html"
    model = Recetario
    form_class = CreateRecetario
    

    def get_form_kwargs(self):
        kwargs = super(RecetarioCreate, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    success_url = reverse_lazy('misreceticas')

## Clase para actualizar un recetario

class RecetarioUpdate(UpdateView):
    template_name = "recetas/formGeneral.html"
    model = Recetario
    fields = ['nombrer','descripcionr']
    success_url = reverse_lazy('misreceticas')

## Clase para borrar un recetario

class RecetarioDelete(DeleteView):
    template_name = "recetas/formGeneral.html"
    model = Recetario
    success_url = reverse_lazy('misreceticas')

## Clase para mostrar la lista de las recetas asociadas con mi cuenta

class MisReceticasListView(ListView):

	def get_context_data(self, **kwargs):
		context = super(MisReceticasListView, self).get_context_data(**kwargs)
		return context
	def get_queryset(self):
		sessionIdusuario = self.request.user.id
		result = Recetario.objects.filter(idusuario=sessionIdusuario)
        	return result

## Clase para Mostrar la lista de recetas 

class RecetarioRecetasUsuarioListView(ListView):
	
	def get_context_data(self, **kwargs):
		context = super(RecetarioRecetasUsuarioListView, self).get_context_data(**kwargs)
		return context

	def get_queryset(self):
		result = Receta.objects.filter(idrecetario=self.kwargs.get('pk', None))
        	return result

## Clase para mostrar la lista de pasos 

class PasosListView(ListView):
	
	def get_context_data(self, **kwargs):
		context = super(PasosListView, self).get_context_data(**kwargs)
		context['receta']= self.kwargs.get('pk', None)
		return context

	def get_queryset(self):
		result = Pasos.objects.filter(idreceta=self.kwargs.get('pk', None))
        	return result

## Clase para crear pasos

class PasoCreate(CreateView):
    template_name = "recetas/formGeneral.html"
    model = Pasos
    form_class = CreatePaso

    def get_form_kwargs(self):
        kwargs = super(PasoCreate, self).get_form_kwargs()
        kwargs['receta'] = self.kwargs.get('pk', None)
        return kwargs
    success_url = reverse_lazy('misreceticas')

## Clase para actualizar los pasos

class PasoUpdate(UpdateView):
    template_name = "recetas/formGeneral.html"
    model = Pasos
    fields = ['pasonumero','contenido']
    success_url = reverse_lazy('misreceticas')

## Clase para borrar los pasos

class PasoDelete(DeleteView):
    template_name = "recetas/formGeneral.html"
    model = Pasos
    success_url = reverse_lazy('misreceticas')



#################### Ingredientes

## Clase para mostrar los ingredientes

class IngredientesListView(ListView):
	def get_context_data(self, **kwargs):
		context = super(IngredientesListView, self).get_context_data(**kwargs)
		context['receta']=  self.kwargs.get('pk', None)
		return context

	def get_queryset(self):
		result =  IngredienteXReceta.objects.select_related().filter(idreceta=self.kwargs.get('pk', None))
        	return result

## Clase para crear ingredientes

class IngredienteCreate(CreateView):
    template_name = "recetas/formGeneral.html"
    form_class = CreateIngrediente

    def get_form_kwargs(self):
        kwargs = super(IngredienteCreate, self).get_form_kwargs()
        kwargs['receta'] = self.kwargs.get('pk', None)
        return kwargs
    success_url = reverse_lazy('misreceticas')

## Clase para borrar ingredientes

class IngredienteDelete(DeleteView):
    template_name = "recetas/formGeneral.html"
    model = Pasos
    success_url = reverse_lazy('misreceticas')


