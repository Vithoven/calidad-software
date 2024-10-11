from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager , PermissionsMixin 
from .enumeraciones import *
# Create your models here.

class producto(models.Model):
    nombre=models.CharField(max_length=50, null=False ,unique=True)
    stock=models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(1000)])
    descripción=models.CharField(max_length=150, null=False) 
    precio=models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(999999)])
    foto=models.ImageField(upload_to='producto',null=False)
    
    def __str__(self):
        return f"{self.nombre}"

class Usuariomanager(BaseUserManager):
    def create_user(self, correo, password=None, **extra_fields):
        if not correo:
            raise ValueError("El correo es obligatorio")
        usuario = self.model(correo=self.normalize_email(correo), **extra_fields)
        usuario.set_password(password)
        usuario.save()
        return usuario
    def create_superuser(self, correo, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(correo=correo, password=password, **extra_fields)   
    
class Usuario(AbstractBaseUser,PermissionsMixin):
    run = models.CharField( "rut" ,max_length=10 ,primary_key=True ) 
    correo = models.EmailField("correo", max_length=150 , unique=True)
    nombre = models.CharField("nombre", max_length=50)
    apellido = models.CharField("apellido", max_length=50)
    telefono= models.CharField("telefono", max_length=9)
    comuna= models.CharField("comuna", max_length=50)
    direccion= models.CharField("direccion", max_length=50)
    is_staff = models.BooleanField("empleado",default=False)
    is_superuser = models.BooleanField("superuser",default=False)
    es_baneado = models.BooleanField("baneado", default=False)
    
    USERNAME_FIELD="correo"
    objects=Usuariomanager()
    REQUIRED_FIELDS=["run","nombre","apellido","telefono","comuna","direccion"]

class Tarjeta(models.Model):  
    uusuario=models.ForeignKey("mi_web.Usuario", verbose_name=("usuario"), on_delete=models.CASCADE , null=True)
    tarjeta_de_credito = models.CharField("numero tarjeta", max_length=16, unique=True)
    fecha_de_vencimiento = models.CharField("fecha vencimiento", max_length=5)
    codigo_de_seguridad = models.CharField("cv",max_length=3)
    
    def __str__(self):
        numero_str = str(self.tarjeta_de_credito)
        return f'**** **** **** {numero_str[-4:]}'


class CarritoDeCompras(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE )
    productos = models.ManyToManyField(producto, through='ItemCarrito')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Carrito de {self.user.nombre}'
    
    @property
    def cant(self):
        itens = ItemCarrito.objects.filter(carrito=self.pk)
        
        return len(itens)
class ItemCarrito(models.Model):
    carrito = models.ForeignKey(CarritoDeCompras, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.cantidad} of {self.producto.nombre}'
    
class Boleta(models.Model):
    user = models.ForeignKey('Usuario', verbose_name=("Usuario") ,on_delete=models.DO_NOTHING)
    carritoDeCompra =  models.ForeignKey(CarritoDeCompras,verbose_name=("CarritoDeCompra") , on_delete=models.DO_NOTHING)
    metodoDePago = models.ForeignKey(Tarjeta , verbose_name=("Tarjeta") ,on_delete=models.DO_NOTHING)
    estado = models.CharField("estado",max_length=20, choices=ESTADO_ENVIO,default="ALMACEN")
    telefono2 = models.CharField("telefono2", max_length=9)
    comuna2 = models.CharField("comuna2", max_length=50)
    direccion2 = models.CharField("direccion2", max_length=50)
    fecha_emision = models.DateTimeField("fecha_emision",auto_now_add=True)
    rut_receptor = models.CharField("RUT del Receptor", max_length=10)
    nombre_receptor = models.CharField("Nombre del Receptor", max_length=100)
    
    def __str__(self):
        return f'Boleta {self.id} - {self.user.nombre}'
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Asignar los productos del carrito a la boleta
            
class ProductoBoleta(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    producto = models.CharField("producto",max_length=50)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.cantidad} de {self.producto} en Boleta {self.boleta.id}'
    
class Bloqueo(models.Model):
    usuario = models.ForeignKey("mi_web.Usuario", on_delete=models.CASCADE, related_name='bloqueos')
    razon = models.TextField("Razón del Bloqueo", max_length=500)
    fecha_bloqueo = models.DateTimeField("Fecha de Bloqueo", auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.razon}"

    class Meta:
        verbose_name = "Bloqueo"
        verbose_name_plural = "Bloqueos"
        ordering = ['-fecha_bloqueo']
          
class Desbloqueo(models.Model):
    usuario = models.ForeignKey("mi_web.Usuario", on_delete=models.CASCADE, related_name='Desbloqueo')
    razon = models.TextField("Razón del Desbloqueo", max_length=500)
    fecha_desbloqueo = models.DateTimeField("Fecha de Desbloqueo", auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.razon}"

    class Meta:
        verbose_name = "Desbloqueo"
        verbose_name_plural = "Desbloqueo"
        ordering = ['-fecha_desbloqueo']

class Reclamo(models.Model):
    usuario = models.ForeignKey("mi_web.Usuario", verbose_name=("Usuario"), on_delete=models.CASCADE)
    boleta = models.ForeignKey(Boleta, verbose_name=("Boleta"),on_delete=models.CASCADE)
    tipo = models.CharField("Tipo de reclamo", max_length=20, choices=MOTIVO_REEMBOLSO)
    estado = models.CharField("Estado del reclamo", max_length=20, choices=ESTADOS_RECLAMO, default='PENDIENTE')
    descripcion = models.TextField("Descripción del reclamo")
    fecha_creacion = models.DateTimeField("Fecha de creación", auto_now_add=True)

    def __str__(self):
        return f'Reclamo {self.id} - {self.usuario.nombre}'

class Provincia(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey("mi_web.Provincia", verbose_name=("provincia"), on_delete=models.CASCADE)

    class Meta:
        unique_together = ['nombre', 'provincia']

    def __str__(self):
        return f'{self.nombre}'
