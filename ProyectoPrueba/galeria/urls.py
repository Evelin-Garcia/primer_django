from django.urls import path
from . import views #importamos las vistas de la aplicacion

app_name='galeria' #namespace de la aplicacion galeria

urlpatterns = [
    path('', views.index, name='index'), #Definir la ruta/página principal de la aplicacion galeria
]
