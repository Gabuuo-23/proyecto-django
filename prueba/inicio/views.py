from django.shortcuts import render,HttpResponse

# Create your views here.
def principal(request):
    return render (request,"inicio/principal.html")

def Minombre(request):
    return render(request,"inicio/nombre.html")

def Contacto(request):
    return render(request,"inicio/contacto.html")

def Formulario(request):
    return render(request,"inicio/formulario.html")

def Ejemplo(request):
    return render(request,"inicio/ejemplo.html")



