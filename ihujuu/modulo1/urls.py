from turtle import home
from django.contrib import admin
from django.urls import path, include
from modulo1.views import *
from .views import registro_usuario
from django.urls import path
from . import views
from django.urls import path
from . import views
from .views import base_view





urlpatterns = [
#----------------------------------evento----------------------------------------------------------------------------------------------------------------------------#

    path('Evento/', ListadoEventos.as_view(template_name = "crud\evento\index.html"), name='leerevento'),
    path('Evento/crear/', EventosCrear.as_view(template_name ="crud\evento\evento_crear.html"), name='crearevento'),
    path('Evento/<int:pk>/', EventosDetalle.as_view(template_name ="crud\evento\evento_detalle.html"), name='detalleevento'),
    path('Evento/<int:pk>/actualizar/', EventosActualizar.as_view(template_name ="crud\evento\evento_actualizar.html"), name='actualizarevento'),
    path('Evento/<int:pk>/eliminar/', EventosEliminar.as_view(template_name ="crud\evento\evento_eliminar.html"), name='eliminarevento'),

#----------------------------------evento----------------------------------------------------------------------------------------------------------------------------#

#----------------------------------cronograma----------------------------------------------------------------------------------------------------------------------------#
    path('Cronograma/',  ListadoCronograma.as_view(template_name = "crud\cronograma\index.html"), name='leerCronograma'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('Cronograma/crear', CronogramaCrear.as_view(template_name = "crud\cronograma\crear.html"), name='crearCronograma'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Administradors o registro 
    path('Cronograma/detalle/<int:pk>', CronogramaDetalle.as_view(template_name = "crud\cronograma\detalle.html"), name='detalleCronograma'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Administradors o registro de la Base de Datos 
    path('Cronograma/editar/<int:pk>', CronogramaActualizar.as_view(template_name = "crud\cronograma\eactualizar.html"), name='actualizarCronograma'), 
    # La ruta 'eliminar' que usaremos para eliminar un Administradors o registro de la Base de Datos 
   path('Cronograma/eliminar/<int:pk>/', CronogramaEliminar.as_view(template_name = "crud\cronograma\eliminar"), name='eliminarCronograma'),
#---------------------------------cronograma----------------------------------------------------------------------------------------------------------------------------#

]