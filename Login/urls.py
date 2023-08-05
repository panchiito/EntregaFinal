from django.urls import path
from Login import views
from Login.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('index', views.index, name="Index"), 
    path('', views.index, name="Index"), 
    path('padre', views.padre, name="Padre"), 
    path('sobremi', views.sobremi, name="SobreMi"), 
    path('formPubli', views.formPubli, name="FormularioPublicacion"), 
    path('leerPublicaciones', views.leerPublicaciones, name="LeerPublicaciones"), 
    path('eliminarPublicacion/<publicacion_titulo>/', views.eliminarPublicacion,name="EliminarPublicacion"), 
    path('editarPublicacion/<publicacion_titulo>/', views.editarPublicacion,name="EditarPublicacion"), 
    path("publicaciones/list/", PublicacionList.as_view(), name="List"), 
    path("publicacion/<pk>", PublicacionDetalle.as_view(), name="Detail"), 
    path("publicacion/nuevo/<pk>", PublicacionCreacion.as_view(), name="New"), 
    path("publicacion/editar/<pk>", PublicacionUpdate.as_view(), name="Edit"), 
    path("publicacion/borrar/<pk>", PublicacionDelete.as_view(), name="Delete"),
    path('login', views.login_request, name="Login"), 
    path('register', views.register, name="Register"), 
    path('logout', LogoutView.as_view(template_name="logout.html"), name="Logout"), 
    path('receta/', views.receta, name='Receta'), 



]
