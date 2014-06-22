from django import forms
from models import Receta

class CreateRecetaForm(forms.ModelForm):
	class Meta:
       		model = Receta
   		idreceta = forms.CharField()
    		nombre = forms.CharField()
    		tiempo = forms.CharField()
		descripcion = forms.CharField(widget=forms.Textarea)
