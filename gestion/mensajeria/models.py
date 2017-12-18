from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mensajes(models.Model):
    """A model para los mensajes"""
    
    titulo = models.CharField("Titulo", max_length=80, default="vane no te duermas")
    cuerpo = models.CharField("Cuerpo del mensaje", max_length=200)
    usuarioRemitente = models.ForeignKey(User,related_name="Usuario_Remitente",  blank=True, null=True, on_delete=models.CASCADE)    
    usuarioDesteinatario = models.ForeignKey(User, related_name="Usuario_Desteinatario", blank=False, null=False, on_delete=models.CASCADE)    
    