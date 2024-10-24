from django.shortcuts import render
from .models import Articulo

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')#Renderiza la plantilla index.html

def articulos_list(request):
    articulos= Articulo.objects.all() #obtiene todos los articulos de la tabla de la BBDD
    return render(request, 'blog/articulos_list.html', {'articulos': articulos}) #Renderiza el template de articulos_list