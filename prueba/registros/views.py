from django.shortcuts import render, redirect
from .models import Alumnos, ComentarioContacto  
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404

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

def consultar4(request):
    alumnos = Alumnos.objects.filter(nombre__endswith="an")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar5(request):
    alumnos = Alumnos.objects.filter(matricula__startswith="UTM")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})



