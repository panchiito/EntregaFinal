from ast import Delete
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from Login.forms import *
from Login.models import *
from Mensajes.forms import *
from Mensajes.models import *
from django.core.mail import send_mail


# SECCIONES PRINCIPALES:.

def index(request):
    return render(request, "index.html")

def padre(request):
    return render(request, "padre.html")

def sobremi(request):
    return render(request, "sobremi.html")

def receta(request):
    return render(request, "receta.html")

## CRUD: 

@login_required
def formPubli(request):
    if request.method == "POST":
        miFormulario = PublicacionFormulario(request.POST, request.FILES)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            publicacion = Publicacion(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], cuerpo=informacion['cuerpo'], autor=informacion['autor'], fecha=informacion['fecha'], imagen=informacion['imagen'])
            publicacion.save()
            return render(request, "index.html")
    else:
        miFormulario = PublicacionFormulario()
    return render(request, "formPubli.html", {"miFormulario": miFormulario})

@login_required
def leerPublicaciones(request):
    publicaciones = Publicacion.objects.all()
    contexto = {"publicaciones": publicaciones}
    return render(request, "leerPublicaciones.html", contexto)

@login_required
def eliminarPublicacion(request, publicacion_titulo):
    publicacion = Publicacion.objects.get(titulo=publicacion_titulo)
    publicacion.delete()
    publicaciones = Publicacion.objects.all()
    contexto = {"publicaciones": publicaciones}
    return render(request, "leerPublicaciones.html", contexto)

@login_required
def editarPublicacion(request, publicacion_titulo):
    publicacion = Publicacion.objects.get(titulo=publicacion_titulo)
    if request.method == "POST":
        miFormulario = PublicacionFormulario(request.POST, request.FILES)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            publicacion.titulo = informacion['titulo']
            publicacion.subtitulo = informacion['subtitulo']
            publicacion.autor = informacion['autor']
            publicacion.cuerpo = informacion['cuerpo']
            publicacion.fecha = informacion['fecha']
            imagen_nueva = informacion.get('imagen')
            if imagen_nueva:
                publicacion.imagen = imagen_nueva
            publicacion.save()
            return render(request, "index.html")
    else:
        miFormulario=PublicacionFormulario(initial={"titulo":publicacion.titulo, "subtitulo":publicacion.subtitulo, "autor":publicacion.autor, "cuerpo":publicacion.cuerpo, "fecha":publicacion.fecha})
    return render(request, "editarPublicacion.html", {"miFormulario": miFormulario, "publicacion_titulo": publicacion_titulo})




## CLASES BASADAS EN VISTAS:

class PublicacionList(ListView):
    model = Publicacion
    template_name = "publicaciones_list.html"

class PublicacionDetalle(DetailView):
    model = Publicacion
    template_name = "publicacion_detalle.html"

class PublicacionCreacion(CreateView):
    model = Publicacion
    success_url = "/publicacion/list"
    fields = ["titulo", "subtitulo", "autor", "cuerpo", "fecha", "imagen"]

class PublicacionUpdate(UpdateView):
    model = Publicacion
    success_url = "/publicacion/list"
    fields = ["titulo", "subtitulo", "autor", "cuerpo", "fecha", "imagen"]

class PublicacionDelete(DeleteView):
    model = Publicacion
    success_url = "/publicacion/list"



## LOGIN


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request, "index.html", {"mensaje":f"Bienvenido {usuario}"} )
            else:
                return render(request, "error1.html" )
        else:
            return render(request, "error2.html" )
    form = AuthenticationForm()
    return render(request, "login.html", {"form":form} )


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "padre.html", {"mensaje": "Usuario creado :)"})
    else:
        form = UserRegisterForm()
    return render(request, "registro.html", {"form": form})



