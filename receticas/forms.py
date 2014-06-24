from django import forms
from models import *
from django.forms import ModelForm, ModelMultipleChoiceField

class CreateRecetaForm(forms.ModelForm):
	class Meta:
       		model = Receta
   		idreceta = forms.CharField()
    		nombre = forms.CharField()
    		tiempo = forms.CharField()
		descripcion = forms.CharField(widget=forms.Textarea)


class CreateRecetario(ModelForm):
    class Meta:
        model = Recetario
	exclude = ('idrecetario','idusuario')

    nombrer = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={'placeholder': 'Nombre'})
    )
    descripcionr = forms.CharField(
        label='Descripcion',
        widget=forms.TextInput(attrs={'placeholder': 'Descripcion'})
    )
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(CreateRecetario, self).__init__(*args, **kwargs)
	
    def save(self, commit=True, force_insert=False, force_update=False, *args, **kwargs):
        m = super(CreateRecetario, self).save(commit=False, *args, **kwargs)
        m.idrecetario = Recetario.objects.latest('idrecetario').idrecetario + 1
	m.idusuario_id = self.request.user.id
	m.save()


class CreateReceta(ModelForm):
    class Meta:
        model = Receta
	exclude = ('idreceta','idrecetario')

    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={'placeholder': 'Nombre'})
    )
    tiempo = forms.CharField(
        label='Tiempo',
        widget=forms.TextInput(attrs={'placeholder': 'Tiempo'})
    )
    descripcion = forms.CharField(
        label='Descripcion',
        widget=forms.Textarea(attrs={'placeholder': 'Descripcion'})
    )

    def __init__(self, *args, **kwargs):
        self.recetario = kwargs.pop('recetario')
        super(CreateReceta, self).__init__(*args, **kwargs)
	
    def save(self, commit=True, force_insert=False, force_update=False, *args, **kwargs):
        m = super(CreateReceta, self).save(commit=False, *args, **kwargs)
        m.idreceta = Receta.objects.latest('idreceta').idreceta + 1
	m.idrecetario_id = self.recetario
	m.save()

class CreatePaso(ModelForm):
    class Meta:
        model = Pasos
	exclude = ('idpaso','idreceta')

    pasonumero = forms.CharField(
        label='Paso numero',
        widget=forms.TextInput(attrs={'placeholder': 'Paso numero'})
    )
    contenido = forms.CharField(
        label='Contenido',
        widget=forms.TextInput(attrs={'placeholder': 'Contenido'})
    )

    def __init__(self, *args, **kwargs):
        self.receta = kwargs.pop('receta')
        super(CreatePaso, self).__init__(*args, **kwargs)
	
    def save(self, commit=True, force_insert=False, force_update=False, *args, **kwargs):
        m = super(CreatePaso, self).save(commit=False, *args, **kwargs)
        m.idpaso = Pasos.objects.latest('idpaso').idpaso + 1
	m.idreceta_id = self.receta
	m.save()


class CreateIngrediente(ModelForm):
    class Meta:
        model = IngredienteXReceta

	exclude = ('idreceta','idingrediente',)
	 
    def __init__(self, *args, **kwargs):
        self.receta = kwargs.pop('receta')
        super(CreateIngrediente, self).__init__(*args, **kwargs)
	self.fields['idingredienteTemp'] = forms.ChoiceField(choices= [ (o, o.articulo  ) for o in Ingrediente.objects.all()])
	
    def save(self, commit=True, force_insert=False, force_update=False, *args, **kwargs):
        m = super(CreateIngrediente, self).save(commit=False, *args, **kwargs)
        #m.idpaso = Pasos.objects.latest('idpaso').idpaso + 1
	m.idingrediente = Ingrediente.objects.get(pk=self.fields['idingredienteTemp'])     
	m.idreceta_id = self.receta
	m.save()


	
#o.idingrediente.articulo
    def save(self, commit=True, force_insert=False, force_update=False, *args, **kwargs):
        m = super(CreateIngrediente, self).save(commit=False, *args, **kwargs)
	m.idreceta_id = self.receta
	m.save()

