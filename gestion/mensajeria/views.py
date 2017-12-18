from django.shortcuts import render
from mensajeria.models import Mensajes
from django.contrib.auth.models import User
# Create your views here.


qs = User.objects.filter(id="2")
m = Mensajes(titulo="juanito bobo", cuerpo="hola", usuarioDesteinatario=qs[0])
m.save()