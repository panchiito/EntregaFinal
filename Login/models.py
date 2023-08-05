from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lector(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    def __str__(self):
        return f"Username: {self.username} - Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"

class Moderador(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    def __str__(self):
        return f"Username: {self.username} - Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"


class Publicacion(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=30)
    cuerpo = models.TextField(max_length=999999)
    autor = models.CharField(max_length=30)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True)
    def __str__(self):
        return f"Titulo: {self.titulo} - Subtitulo: {self.subtitulo} - Cuerpo: {self.cuerpo} - Autor: {self.autor} - Fecha: {self.fecha} - Imagen: {self.imagen}"
