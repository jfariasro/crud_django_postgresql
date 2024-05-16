from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

def inicio(request):
    return render(request, 'pages/inicio.html')

def nosotros(request):
    return render(request, 'pages/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crear_libro(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        return redirect('libros')

    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar_libro(request, id):
    libro = Libro.objects.get(idlibro=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)

    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')

    return render(request, 'libros/editar.html', {'formulario': formulario})

def eliminar_libro(request, id):
    libro = Libro.objects.get(idlibro=id)
    libro.delete()
    return redirect('libros')