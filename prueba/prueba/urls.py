"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registros import views as views_registros
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_registros.registros, name="Principal"),
    #path('',views.principal, name="Principal"),
    path('Minombre/',views.Minombre, name="Minombre"),
    path('Contacto/',views_registros.contacto, name="Contacto"),
    path('Formulario/',views.Formulario, name="Formulario"),
    path('Ejemplo/',views.Ejemplo, name ="ejemplo"),
    path('registrar/',views_registros.registrar,name="Registrar"),
    path('consultaComentarios/', views_registros.registrar, name = "ConsultaComentarios"),
    path('eliminarComentario/<int:id>/',views_registros.eliminarComentarioContacto,name='Eliminar'),
    path('editarComentario/<int:id>/',views_registros.editarComentario,name = "Editar"),
    path('consultas/',views_registros.Consultas, name="Consultas"),

    path('consultar1/',views_registros.consultar1, name="Consultar1"),
    path('consultar2/',views_registros.consultar2, name="Consultar2"),
    path('consultar3/',views_registros.consultar3, name="Consultar3"),
    #tarea lunes
    path('consultar4/',views_registros.consultar4, name="Consultar4"),
    path('consultar5/',views_registros.consultar5, name="Consultar5"),
    #practica
    path('consultar6/',views_registros.consultar6, name="Consultar6"),
    path('consultar7/',views_registros.consultar7, name="Consultar7"),
    path('consultar8/',views_registros.consultar8, name="Consultar8"),
    path('consultasSQL/',views_registros.consultasSQL, name="ConsultasSQL"),
    path('consultarcomentario/',views_registros.consultarcomentario, name="ConsultarComentario"),
    path('consultarexpresion/',views_registros.consultarexpresion, name="ConsultarExpresion"),
    path('consultarusuario/',views_registros.consultarusuario, name="ConsultarUsuario"),
    path('consultarendswith/',views_registros.consultarendswith, name="ConsultarEndsWith"),
    path('consultarstard/',views_registros.consultarstard, name="ConsultarStartsWith"),
    path('subir/',views_registros.archivos, name="subir"),
    path('seguridad/',views_registros.seguridad, name="Seguridad"),
    path('seguridad/',views_registros.seguridad, name="Seguridad"),

    #path('formEditarComentario/<int:id>/',views_registros.consultarComentarioIndividual,name='ConsultaIndividual'),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)