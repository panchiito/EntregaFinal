
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Mensajes import views
from Mensajes.views import *

urlpatterns = [

    path('lista_mensajes/', views.lista_mensajes, name='lista_mensajes'),
    path('lista_usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('contact', views.contact, name="contact"),
    path('enviar_mensaje/<int:receptor_id>/', views.enviar_mensaje, name='enviar_mensaje'),
    path('', views.index2, name="index2"), 






]