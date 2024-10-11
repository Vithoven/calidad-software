from django.contrib import admin
from .models import producto , Usuario , Tarjeta , CarritoDeCompras ,Reclamo ,Desbloqueo ,Bloqueo ,Boleta ,Provincia,Comuna
# Register your models here.

class admProducto(admin.ModelAdmin):
    list_display = ['id' ,'nombre','stock']
    #list_editable
     
class admUsuarios(admin.ModelAdmin):
    list_display = ['run' ,'nombre','correo']
    #list_editable
class admCarritos(admin.ModelAdmin):
    list_display = ['id' ,'user']
    #list_editable
class admTarjeta(admin.ModelAdmin):
    list_display = ['tarjeta_de_credito' , 'uusuario']
    #list_editable    

class admReclamo(admin.ModelAdmin):
    list_display = ['id' ,'descripcion' ,'estado']
    #list_editablev
class admDesbloqueo(admin.ModelAdmin):
    list_display = ['id' ,'razon']
    #list_editable
class admBloqueo(admin.ModelAdmin):
    list_display = ['id' ,'razon']
    #list_editable    

class admBoleta(admin.ModelAdmin):
    list_display = ['id' ,'user','estado','fecha_emision','nombre_receptor']
    #list_editable      

class admProvincia(admin.ModelAdmin):
    list_display = ['id' ,'nombre']
    #list_editable  
    
class admComuna(admin.ModelAdmin):
    list_display = ['id' ,'nombre']
    #list_editable  
# Register your models here.

admin.site.register(producto, admProducto)
admin.site.register(Usuario, admUsuarios)
admin.site.register(Tarjeta, admTarjeta)
admin.site.register(CarritoDeCompras, admCarritos)
admin.site.register(Reclamo, admReclamo)
admin.site.register(Desbloqueo, admDesbloqueo)
admin.site.register(Provincia, admProvincia)
admin.site.register(Boleta, admBoleta)
admin.site.register(Bloqueo, admBloqueo)
admin.site.register(Comuna, admComuna)