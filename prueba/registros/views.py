from django.shortcuts import render, redirect
from .models import Alumnos, ComentarioContacto  
from .forms import ComentarioContactoForm


def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {'alumnos': alumnos})


def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Consulta Comentarios') 
    else:
        form = ComentarioContactoForm()
    
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/consultaComentarios.html", {
        'form': form,
        'comentarios': comentarios
    })
    

def contacto(request):
    form = ComentarioContactoForm()
    return render(request, "registros/contacto.html", {'form': form})

#ver