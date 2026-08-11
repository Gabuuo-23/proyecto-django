from urllib import request

from django.shortcuts import render, redirect
from .models import Alumnos, ComentarioContacto ,Archivos
from .forms import ComentarioContactoForm,FormArchivos
from django.shortcuts import get_object_or_404
import datetime
import django.contrib.messages as messages

def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {'alumnos': alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ConsultaComentarios') 
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

def eliminarComentarioContacto(request,id,confirmacion = 'registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id = id)
    if request.method =='POST':
        comentario.delete()
        comentarios =ComentarioContacto.objects.all()
        return render (request,"registros/consultaComentarios.html",{'consultaComentarios':comentario})
    return render(request, confirmacion, {'objec': comentario})

def editarComentario(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)

    if request.method == 'POST':
        comentario.usuario = request.POST.get('usuario')
        comentario.mensaje = request.POST.get('mensaje')
        comentario.save()

        return redirect('ConsultaComentarios')

    return render(request, "registros/editarComentario.html", {
        'comentario': comentario
    })
    
def consultarComentarioIndividual(request, id):
    comentario = ComentarioContacto.objects.get(id=id)
    return render(request,"registros/editarComentario.html",{'comentario':comentario})

def Consultas(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar1(request):
    alumnos = Alumnos.objects.filter(carrera="TI")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar2(request):
    alumnos = Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar3(request):
    alumnos=Alumnos.objects.all().only("matricula","nombre","carrera","turno","image")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

#tarea lunes
def consultar4(request):
    alumnos = Alumnos.objects.filter(nombre__endswith="an")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

#tarea lunes
def consultar5(request):
    alumnos = Alumnos.objects.filter(matricula__startswith="UTM")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar6(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
    fechaInicio = datetime.date(2026, 8, 3)
    fechaFin = datetime.date(2026, 8, 10)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar8(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains='No inscrito')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT id, matricula,nombre, carrera, turno, image FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request,"registros/consultas.html", {'alumnos':alumnos})

def consultarcomentario(request):
    comentarios = ComentarioContacto.objects.filter(created__range=["2026-06-20", "2026-08-4"])
    return render( request,"registros/consultaComentarios.html",{'comentarios': comentarios})

def consultarexpresion(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__icontains="Tigres")
    return render(request,"registros/consultaComentarios.html",{"comentarios": comentarios})

def consultarusuario(request):
    comentarios = ComentarioContacto.objects.filter(usuario="Edgar")
    return render(request,"registros/consultaComentarios.html",{"comentarios": comentarios})

# tarea lunes
def consultarendswith (request):
    # __endswith busca mensajes que finalicen con ese texto
    comentarios = ComentarioContacto.objects.filter(mensaje__endswith="es")
    return render(request, "registros/consultaComentarios.html", {'comentarios': comentarios})

# tarea lunes
def consultarstard(request):
    # __startswith busca mensajes que inicien con ese texto
    comentarios = ComentarioContacto.objects.filter(mensaje__startswith="le")
    return render(request, "registros/consultaComentarios.html", {'comentarios': comentarios})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST.get('titulo')
            descripcion = request.POST.get('descripcion')
            archivo = request.FILES.get('archivo')
            insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request, "registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario.")
    else:
        return render(request, "registros/archivos.html",{'archivos':Archivos})

def seguridad(request):
    return render(request,"inicio/seguridad.html")

def seguridad(request):
    nombre = request.GET.get('nombre')
    return render(request,"registros/seguridad.html",{'nombre':nombre})