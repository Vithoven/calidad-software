from .models import CarritoDeCompras 
from django.http import HttpRequest

def carrito(request:HttpRequest):
    if request.user.is_authenticated:
        carito = CarritoDeCompras.objects.get(user=request.user)
        return {"carrito":carito} 
    return {}