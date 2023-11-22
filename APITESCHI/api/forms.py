from django import forms

class MiFormulario(forms.Form):
    campo1 = forms.CharField(label='Campo 1')
    campo2 = forms.IntegerField(label='Campo 2')

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True, max_length=20)
    email = forms.CharField(label='Email',required=True, max_length=40)
    contenido = forms.CharField(label='Contenido', max_length=400 widget=forms.Textarea )