from django import forms

class MiFormulario(forms.Form):
    campo1 = forms.CharField(label='Campo 1')
    campo2 = forms.IntegerField(label='Campo 2')

class FormularioContacto (forms.Forms):
    nombre=forms.charFiel(label='Nombre',required=true, max_length=20)
    email=forms.charFiel(label='Email',required=true, max_length=40)
    contenido=forms.charFiel(label='Contenido', max_length=400 widget=forms.Textarea)