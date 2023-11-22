from django.shortcuts import render, redirect
from rest_framework.views import APIView 
from django.http import HttpResponse
import csv
from django.shortcuts import render
from django import forms
from django.core.mail import EmailMassage
from .forms import FormularioContacto
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

def correo (request):
    formulario_contacto=FormularioContacto()
    if request.mmethod=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("Nombre")
            email=request.POST.get("Email")
            contenido=request.POST.get("Contenido")
            email=EmailMessagew("Mensaje de app Django",
            "El usuario con nombre {} con la direccion {} escribe lo siguiente:\n\n{}".format(nombre, email, contenido),
            '',
            ["ricardomendietajr222@gmail.com"],
            reply_to=[email])

            try:
                email.send()
                return redirect("/correo/?valido")
            except:
                return redirect("/correo/?novalido")

    return render (request, "correo/correo.html",{'mi formulario':formulario_contacto})            

