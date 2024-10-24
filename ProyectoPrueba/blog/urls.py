from django.urls import path
from . import views #importamos las vistas de la aplicacion

app_name='blog' #namespace de la aplicacion blog

urlpatterns = [
    path('', views.index, name='index'),#Define la ruta/página principal de la aplicacion blog
    path('articulos/', views.articulos_list, name='articulos_list'),
]
