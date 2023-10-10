from django.shortcuts import render
from rest_framework.views import APIView 
# Create your views here.

class index (APIView):
    template_name="index.html"
    def get (self,request):
        return render(request,self.template_name)

class login (APIView):
    template_name="login.html"
    def get (self,request):
        return render(request,self.template_name)