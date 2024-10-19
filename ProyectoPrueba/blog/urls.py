from django.urls import path
from . import views #importamos las vistas de la aplicacion

urlpatterns = [
    path('', views.home, name='home'), #Definir la ruta principal de la aplicacion blog
]
