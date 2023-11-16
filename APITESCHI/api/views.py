from django.shortcuts import render
from rest_framework.views import APIView 
from django.http import HttpResponse
import csv
from django.shortcuts import render
from .forms import MiFormulario
from django import forms
# Create your views here.

class index (APIView):
    template_name="index.html"
    def get (self,request):
        return render(request,self.template_name)

class login (APIView):
    template_name="login.html"
    def get (self,request):
        return render(request,self.template_name)

class register (APIView):
    template_name="register.html"
    def get (self,request):
        return render(request,self.template_name)
    
def exportar_dispotivos_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dispositivo.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nombre_del_dispositivo ', 'Quien_lo_realiza', 'Descripción'])
    
    dispositivo = dispositivo.objects.all()
    for dispositivo in dispositivo:
        writer.writerow([dispositivo.Nombre_del_dispositivo , dispositivo.Quien_lo_realiza, dispositivo.descripcion])

    return response
def mi_vista(request):
    if request.method == 'POST':
        formulario = MiFormulario(request.POST)
        if formulario.is_valid():
            # Realizar acciones con los datos del formulario
            # Por ejemplo, guardar en la base de datos
            pass
    else:
        formulario = MiFormulario()

    return render(request, 'mi_aplicacion/mi_template.html', {'formulario': formulario})
