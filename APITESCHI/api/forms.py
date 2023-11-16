from django import forms

class MiFormulario(forms.Form):
    campo1 = forms.CharField(label='Campo 1')
    campo2 = forms.IntegerField(label='Campo 2')