from django.shortcuts import render
from rest_framework.views import APIView 
from django.http import HttpResponse
import csv
from .models import dispositivo 
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