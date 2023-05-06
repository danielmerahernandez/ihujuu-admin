from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from contextlib import _RedirectStream, redirect_stdout
from modulo1.models import *
from django.urls import reverse
from django.contrib.auth import login, authenticate
#importo el modelo de la base de datos de models.py
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 

# Habilitamos el uso de mensajes en Django
from django.contrib import messages
# Habilitamos los formularios en Django
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from . import views









# Create your views here.
def Login(request):
    return render (request, "login.html")

def Home2(request):
    return render(request, "tours.html")

def Home1(request):
    return render(request, "index3.html")

def Login(request):
    return render (request, "login.html")

def Discografia(request):
    return render (request, "vista-usuario/discography.html")

def Index(request):
    return render (request, "vista-usuario/index-vistap.html")

def Acercade(request):
    return render (request, "vista-usuario/about.html")

def Contactenos(request):
    return render (request, "vista-usuario/contact.html")

def Tours(request):
    return render (request, "vista-usuario/tours.html")

def Blog(request):
    return render (request, "vista-usuario/blog.html")

def Nav(request):
    return render (request, "previa_nav.html")

#-----------------------------modelo vista template---------------------------#

#------------------------------para llenar la base de datos-------------------#

#-----------------------------evento--------------------------------------------#

class ListadoEventos(ListView):
     model = Eventos
    
class EventosCrear(SuccessMessageMixin, CreateView):
    model = Eventos
    form = Eventos
    fields = "__all__"
    success_message ='Evento creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerevento') 

class EventosDetalle (DetailView):
    model =Eventos

class  EventosActualizar(SuccessMessageMixin,UpdateView):
    model =  Eventos
    form = Eventos
    fields = "__all__"  
    success_message = 'evento Actualizado Correctamente !' 

    def get_success_url(self):               
        return reverse('modulo1:leerevento') 
class EventosEliminar(SuccessMessageMixin, DeleteView): 
    model = Eventos
    form = Eventos
    fields = "__all__"     
 
    
    def get_success_url(self): 
        success_message = 'evento Eliminado Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerevento') 
    #-----------------------------evento--------------------------------------------#


#------------------------------------------cronograma-------------------------------------#
class ListadoCronograma(ListView):
     model = Cronograma
    
class CronogramaCrear(SuccessMessageMixin, CreateView):
    model = Cronograma
    form = Cronograma
    fields = "__all__"
    success_message ='Cronograma creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerCronograma') 

class CronogramaDetalle (DetailView):
    model = Cronograma

class  CronogramaActualizar(SuccessMessageMixin,UpdateView):
    model =  Cronograma
    form = Cronograma
    fields = "__all__" 
    success_message = 'Cronograma Actualizado Correctamente !' 

    def get_success_url(self):               
        return reverse('modulo1:leerCronograma') 
class CronogramaEliminar(SuccessMessageMixin, DeleteView): 
    model = Cronograma
    form = Cronograma
    fields = "__all__"     
 
    
    def get_success_url(self): 
        success_message = 'AccionpermitidaHasUsuario Eliminado Correctamente !'
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerCronograma') 



#------------------------------------------cronograma-------------------------------------#