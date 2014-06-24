from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView, DetailView

from views import *



from models import Receta, Recetario

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'receticas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/rece/'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'auth.views.login_user'),
    url(r'^home/$', 'receticas.views.home'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^rece/', 'receticas.views.index'),
    #################Recetas
    url(r'^recetas/(?P<pk>\d+)/$', RecetaDisplayView.as_view(
	context_object_name="receta",
	model=Receta,
	#paginate_by = '5',
	template_name= "recetas/receta.html",
	), name="receta"),
    url(r'^recetas/', RecetaListView.as_view(
	context_object_name="receta",
	model=Receta,
	template_name= "recetas/lista-recetas.html",
	), name="recetas"),
    url(r'recet/add/(?P<pk>\d+)/$', RecetaCreate.as_view(), name='receta_add'),
    url(r'recet/(?P<pk>\d+)/$', RecetaUpdate.as_view(), name='receta_update'),
    url(r'recet/(?P<pk>\d+)/delete/$', RecetaDelete.as_view(), name='receta_delete'),
    ##################Recetarios
    url(r'^recetarios/(?P<pk>\d+)/$', RecetarioDisplayView.as_view(
	context_object_name="recetario",
	#model=Recetario,
	#paginate_by = '5',
	template_name= "recetarios/recetario.html",
	), name="recetario"),
    url(r'^recetarios/', RecetaListView.as_view(
	context_object_name="recetario",
	model=Recetario,
	template_name= "recetarios/lista-recetarios.html",
	), name="recetarios"),
    url(r'^recetasRecetario/(?P<pk>\d+)/$', RecetarioRecetasListView.as_view(
	context_object_name="receta",
	#model=Receta,
	#paginate_by = '5',
	template_name= "recetas/lista-recetas.html",
	), name="receta"),
    url(r'recetario/(?P<pk>\d+)/$', RecetarioUpdate.as_view(), name='recetario_update'),
    url(r'recetario/add/$', RecetarioCreate.as_view(), name='recetario_add'),
    url(r'recetario/(?P<pk>\d+)/delete/$', RecetarioDelete.as_view(), name='recetario_delete'),
    #####################Panel Admin
    url(r'^misreceticas/$', MisReceticasListView.as_view(
	context_object_name="recetario",
	#model=Receta,
	#paginate_by = '5',
	template_name= "recetarios/lista-mis-recetarios.html",
	), name="misreceticas"),
    url(r'^recetasRecetarioUsuario/(?P<pk>\d+)/$', RecetarioRecetasUsuarioListView.as_view(
	context_object_name="receta",
	template_name= "recetas/lista-recetas-usuario.html",
	), name="recetasRecetarioUsuario"),
    ####################PASOS
    url(r'^pasos/(?P<pk>\d+)/$', PasosListView.as_view(
	context_object_name="pasos",
	template_name= "pasos/lista-pasos-receta.html",
	), name="pasosReceta"),
    url(r'paso/(?P<pk>\d+)/$', PasoUpdate.as_view(), name='paso_update'),
    url(r'paso/add/(?P<pk>\d+)/$', PasoCreate.as_view(), name='paso_add'),
    url(r'paso/(?P<pk>\d+)/delete/$', PasoDelete.as_view(), name='paso_delete'),
    ####################Ingredientes

    #####################Junnar

)
