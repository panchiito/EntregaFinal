from django.db import models
from django.contrib.auth.models import User



class Mensaje(models.Model):
    emisor = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    asunto = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
    def __str__(self):
        return f"De: {self.emisor.username} - Para: {self.receptor.username} - Asunto: {self.asunto}"
