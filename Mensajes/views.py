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

## "app mensajeria"

@login_required
def enviar_mensaje(request, receptor_id):
    receptor = User.objects.get(pk=receptor_id)

    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            asunto = form.cleaned_data['asunto']
            contenido = form.cleaned_data['contenido']
            mensaje = Mensaje(emisor=request.user, receptor=receptor, asunto=asunto, contenido=contenido)
            mensaje.save()
            return redirect('lista_mensajes')
    else:
        form = MensajeForm()
    return render(request, 'enviar_mensaje.html', {'form': form, 'receptor': receptor})


@login_required
def lista_mensajes(request):
    mensajes_recibidos = Mensaje.objects.filter(receptor=request.user)
    mensajes_enviados = Mensaje.objects.filter(emisor=request.user)
    contenido = Mensaje.objects.filter(contenido=request.user)
    return render(request, 'lista_mensajes.html', {'mensajes_recibidos': mensajes_recibidos, 'mensajes_enviados': mensajes_enviados, "contenido": contenido})

def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})




## probando una seccion de comentarios para enviar al administrador por mail. 

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.clean_data['topic']
            message = form.clean_data['message']
            sender = form.clean_data.get('sender', 'noreply@example.com')
            send_mail(
                'Feedback from your site, topic: %s' % topic,
                message, sender,
                ["panchiito@hotmail.com"]
            )
            return render(request, 'Login/index.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def index2(request):
    return render(request, "index.html")
