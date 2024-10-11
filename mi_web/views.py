from django.shortcuts import render
from .models import producto , Usuario , Tarjeta , CarritoDeCompras,ItemCarrito ,Boleta,ProductoBoleta
from django.shortcuts import get_object_or_404, redirect
from datetime import date
from .forms import *
from os import remove, path
from django.conf import settings
from django.contrib.auth import logout , login , authenticate ,update_session_auth_hash 
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError 
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        carrito, created = CarritoDeCompras.objects.get_or_create(user=request.user, is_active=True)
    queryset = producto.objects.all()
    filter_form = ProductoFilterForm(request.GET or None)

    if filter_form.is_valid():
        queryset = filter_form.filter_queryset(queryset)
        
    datos = {
        'productos': queryset,
        'filter_form': filter_form,
    }
    return render(request,'vet/index.html',datos)

@login_required
def lista_compras(request):
    queryset = Boleta.objects.all()
    filter_form = BoletaFilterForm(request.GET or None)

    if filter_form.is_valid():
        queryset = filter_form.filter_queryset(queryset)

    context = {
        'boletas': queryset,
        'filter_form': filter_form,
    }
    return render(request,'vet/lista_compras.html',context)

@login_required
def mi_cuenta(request, id):
    carrito, created = CarritoDeCompras.objects.get_or_create(user=request.user, is_active=True)
    usera=get_object_or_404(Usuario,correo=id)
    form=updateUser(instance=usera) 
    form2=upPassUser(user=request.user)
    form3=Tarjeta.objects.filter(uusuario=usera)
    form4= TarjetaForm()
    Boletas = Boleta.objects.filter(user=usera ,estado='ALMACEN'or 'ENVIO' )
    Boletas_completadas = Boleta.objects.filter(user=usera, estado='COMPLETADO' or 'CANCELADO')
    reclamos= Reclamo.objects.filter(usuario=usera) 
    if request.method=="POST":
            form=updateUser(data=request.POST,files=request.FILES,instance=usera)
            form2=upPassUser(data=request.POST,files=request.FILES,user=request.user)
            form4=TarjetaForm(data=request.POST)
            if 'update_profile' and 'change_password'in request.POST:
                if  form.is_valid() and form2.is_valid():
                    form.save()
                    form2.save()
                    update_session_auth_hash(request, form2.user)  # Mantener al usuario autenticado después del cambio de contraseña
                    return redirect(reverse("mi_cuenta",args=[id]))
            if 'update_profile' in request.POST:         
                if  form.is_valid():  
                    form.save()
                    return redirect(reverse("mi_cuenta",args=[id]))
            if 'change_password' in request.POST:          
                if  form2.is_valid():
                    form2.save()    
                    update_session_auth_hash(request, form2.user)  # Mantener al usuario autenticado después del cambio de contraseña  
                    return redirect(reverse("mi_cuenta",args=[id]))   
            if 'agragar_tarjeta' in request.POST: 
                if form4.is_valid():
                    tarjeta = form4.save(commit=False)
                    tarjeta.uusuario=usera
                    tarjeta.save() 
                    return redirect(reverse("mi_cuenta",args=[id]))       
    datos={
        "form":form, 
        "form2":form2,
        "targetas":form3,
        "form4":form4,
        "boletas":Boletas,
        "Boletas_completadas":Boletas_completadas,
        "reclamos":reclamos
    }
    return render(request,'vet/mi_cuenta.html' , datos)

@login_required
def mi_cuenta_td(request,id,usuario):
    tar=get_object_or_404(Tarjeta,id = id)
    form=UpdateTarjetaForm(instance=tar)
    
    if request.method=="POST":
        form=UpdateTarjetaForm(data=request.POST ,instance=tar)
        if 'eliminar_tarjeta' in request.POST:   
            tar.delete()
            return redirect(reverse("mi_cuenta",args=[usuario])) 
        if 'modificar_tarjeta' in request.POST:  
           if form.is_valid():
                form.save()
                return redirect(reverse("mi_cuenta",args=[usuario]))  
      
            
    datos={
        "form":form
    } 
           
    return render(request,'vet/mi_cuenta_td.html' , datos)

def recordando(request):
    return render(request,'vet/recordando.html')

@login_required
def Revision_estado(request,id):
    boleta = get_object_or_404(Boleta, id=id)
    productos_boleta = ProductoBoleta.objects.filter(boleta=boleta)
    form = ActualizarEstadoBoletaForm(request.POST or None, instance=boleta)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        
        return redirect(reverse("Revision_estado",args=[boleta.id]))
    datos = {
        "boleta": boleta,
        "productos_boleta": productos_boleta,
        "form":form
    }
    
    
    return render(request,'vet/Revision_estado.html',datos)

@login_required
def trabajador(request):
    if request.user.is_authenticated:
        carrito, created = CarritoDeCompras.objects.get_or_create(user=request.user, is_active=True)
    return render(request,'vet/trabajador.html')

@login_required
def usuarios_admin(request):
    form_filter = UsuarioFilterForm(request.GET or None)
    usuarios = Usuario.objects.all()
    
    if form_filter.is_valid():
        nombre = form_filter.cleaned_data.get('nombre')
        apellido = form_filter.cleaned_data.get('apellido')
        es_baneado = form_filter.cleaned_data.get('es_baneado')

        if nombre:
            usuarios = usuarios.filter(nombre__icontains=nombre)
        if apellido:
            usuarios = usuarios.filter(apellido__icontains=apellido)
        if es_baneado is not None:
            usuarios = usuarios.filter(es_baneado=es_baneado)
    
    datos = {
        'form_filter': form_filter,
        'usuarios': usuarios,   
    }
    return render(request, 'vet/usuarios_admin.html', datos)

@login_required
def bloqueo_admin(request, id):
    form = BloqueoForm() 
    usera=get_object_or_404(Usuario,correo=id)
    
    if request.method == 'POST':
        bloqueo_form = BloqueoForm(request.POST)
        if bloqueo_form.is_valid():
            bloqueo = bloqueo_form.save(commit=False)
            bloqueo.usuario = usera  # Asignar el usuario al bloqueo
            bloqueo.save()
            
            # Marcar al usuario como baneado
            usera.es_baneado = True
            usera.save()
            return redirect('usuarios_admin')  # Redirigir a la página de administración de usuarios
    
    datos = {
        'form': form
    }
    return render(request, 'vet/bloqueo_admin.html', datos)

@login_required
def desbloqueo_admin(request, id):
    form = DesbloqueoForm() 
    usera=get_object_or_404(Usuario,correo=id)
    
    if request.method == 'POST':
        desbloqueo_form = DesbloqueoForm(request.POST)
        if desbloqueo_form.is_valid():
            bloqueo = desbloqueo_form.save(commit=False)
            bloqueo.usuario = usera  # Asignar el usuario al bloqueo
            bloqueo.save()
            
            # Marcar al usuario como baneado
            usera.es_baneado = False
            usera.save()
            return redirect('usuarios_admin')  # Redirigir a la página de administración de usuarios
    
    datos = {
        'form': form
    }
    return render(request, 'vet/desbloqueo_admin.html', datos)

def login_xd(request):
    if request.method=="POST":
        form = loginForm(data=request.POST)
        if form.is_valid():
            user = form.user_cache  
            if user.es_baneado:
                messages.warning(request, "su usuario esta baneado") 
                messages.warning(request, "si desea asistencia utilize los contactos") 
                return redirect("login")
            login(request ,user)
            if user.is_staff:
                return redirect("trabajador")
            return redirect("index")
        else :
            messages.warning(request, "usuario o contraseña incorrectos") 
            return redirect("login")
    else :
        form = loginForm()
    datos ={
        "form":form
    }
    return render(request,'vet/login.html',datos)

@login_required
def tienda_trabajador(request):
    prod=producto.objects.all()
    form=ProductoForm()
    
    if request.method=="POST":
        form=ProductoForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="tienda_trabajador")
            #Redirigir       
    datos={
        "productos":prod ,
        "form2":form 
    }
    return render(request,'vet/tienda_trabajador.html',datos)

@login_required
def detalleP_trabajador(request, id):
    produc=get_object_or_404(producto,nombre= id)
    form=upProductoForm(instance=produc)
    imagen_anterior = produc.foto.path if produc.foto else None
    
    if request.method=="POST":
            form=upProductoForm(data=request.POST,files=request.FILES,instance=produc)
            if form.is_valid():
                imagen_nueva = form.cleaned_data.get('foto') if len(form.cleaned_data.get('foto').name.split("/")) == 1 else None
                if imagen_nueva and imagen_anterior:
                # Comprobar si la nueva imagen es diferente de la anterior
                    if imagen_nueva.name != path.basename(imagen_anterior):
                    # Eliminar la imagen anterior
                        if path.exists(imagen_anterior):
                            remove(imagen_anterior) 
                form.save()
                return redirect(to="tienda_trabajador")
                
    datos={
        "form":form ,
        "pro":produc
    }
    
    return render(request,'vet/detalleP_trabajador.html',datos)

@login_required
def eliminarP_trabajador(request, id):
    produc=get_object_or_404(producto,nombre= id)
    form=upProductoForm(instance=produc)
    
    if request.method=="POST":
            ItemCarrito.objects.filter(producto=produc).delete()
            produc.delete()
            remove(path.join(str(settings.MEDIA_ROOT).replace('/media',''))+produc.foto.url)
            return redirect(to="tienda_trabajador")
            
    datos={
        "form":form ,
        "pro":produc
    }
    
    return render(request,'vet/eliminarP_trabajador.html',datos)

def cerrar(request):
    logout(request)
    return redirect("index") 

def registro(request):
    form = createUser()
    form2= TarjetaForm()
    
    if request.method=="POST":
        form=createUser(data=request.POST)
        form2=TarjetaForm(data=request.POST)
        
        if form.is_valid():
            usuario=form.save()
            
            if form2.is_valid():
                tarjeta = form2.save(commit=False)
                tarjeta.uusuario=usuario
                tarjeta.save()
                return redirect("login")
                #Redirigir  
    datos= {
        "form":form,
        "form2":form2
        
    }
    
    return render(request , 'vet/registro.html' , datos)

def detalle_producto(request, producto_id):
    producto2 = get_object_or_404(producto, id=producto_id)
    return render(request, 'vet/detalle_producto.html', {'producto': producto2})

@login_required
def agregar_producto(request, producto_id):
    producto2 = get_object_or_404(producto, id=producto_id)
    carrito, created = CarritoDeCompras.objects.get_or_create(user=request.user, is_active=True)
    
    cantidad = int(request.POST.get('cantidad', 1))
    
    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto2, defaults={'cantidad': cantidad})
    if not created:
        item.cantidad += cantidad
        item.save()
    
    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    carrito, created = CarritoDeCompras.objects.get_or_create(user=request.user, is_active=True)
    carrito = get_object_or_404(CarritoDeCompras, user=request.user, is_active=True)
    form = ItemCarritoForm()
    items = ItemCarrito.objects.filter(carrito=carrito) if carrito else []
    for item in items:
        item.subtotal = item.producto.precio * item.cantidad
    total = sum(item.producto.precio * item.cantidad for item in items)
    
    if request.method == 'POST':
        form = ItemCarritoForm(request.POST)
        if form.is_valid():
            item_id = request.POST.get('item_id')
            nueva_cantidad = form.cleaned_data['cantidad']
            item = get_object_or_404(ItemCarrito, id=item_id)
            item.cantidad = nueva_cantidad
            item.save()
            return redirect('ver_carrito')
    datos={
        'items': items, 
        'total': total, 
        'form':form
    }
    return render(request, 'vet/ver_carrito.html', datos)


@login_required
def eliminar_producto(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    item.delete()
    return redirect('ver_carrito')

@login_required
def carrito_login(request):
    form = BoletaForm(user=request.user)
    carrito_de_compras = CarritoDeCompras.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = BoletaForm(request.POST,files=request.FILES,user=request.user)
        if form.is_valid():
            boleta = form.save(commit=False)
            boleta.user = request.user
            boleta.carritoDeCompra = carrito_de_compras  # Asignar el carrito de compras correspondiente
            boleta.save()
            id=boleta.id
             # Asignar los productos del carrito a la boleta
            items_carrito = ItemCarrito.objects.filter(carrito=carrito_de_compras)
            for item in items_carrito:
                ProductoBoleta.objects.create(boleta=boleta, producto=item.producto.nombre, cantidad=item.cantidad)
                 # Reducir el stock del producto vendido
                producto = item.producto
                producto.stock -= item.cantidad
                producto.save()
            # Vaciar el carrito de compras del usuario
            carrito_de_compras.productos.clear()
            
            return redirect(reverse("ver_boleta",args=[id]))
    datos={
        "form":form
        
    }
    return render(request,'vet/carrito_login.html',datos)


@login_required
def ver_boleta(request,id):
    boleta = get_object_or_404(Boleta, id=id)
    productos_boleta = ProductoBoleta.objects.filter(boleta=boleta)

    datos = {
        "boleta": boleta,
        "productos_boleta": productos_boleta
    }
    return render(request,'vet/ver_boleta.html',datos)

@login_required
def Crear_reclamo(request, id):
    form=ReclamoForm()
    boleta = get_object_or_404(Boleta, id=id)
    
    if request.method == 'POST':
        form = ReclamoForm(request.POST,)
        usuario=request.user
        if form.is_valid():
            reclamo = form.save(commit=False)
            reclamo.boleta = boleta  
            reclamo.usuario=usuario
            reclamo.save()
            return redirect(reverse("mi_cuenta",args=[usuario.correo]))
    datos={
        "form":form
        
    }
    return render(request,'vet/Crear_reclamo.html',datos)

@login_required
def reclamos_admin(request):
    reclamos = Reclamo.objects.all()
    form = ReclamoFilterForm(request.GET or None)

    if request.GET:
        if form.is_valid():
            usuario = form.cleaned_data.get('usuarios')
            boleta = form.cleaned_data.get('boletas')
            estado = form.cleaned_data.get('estado')

            if usuario:
                reclamos = reclamos.filter(usuario=usuario)
            if boleta:
                reclamos = reclamos.filter(boleta=boleta)
            if estado:
                reclamos = reclamos.filter(estado=estado)

    datos = {
        'reclamos': reclamos,
        'form': form,
    }
    
    return render(request,'vet/reclamos_admin.html',datos)

@login_required
def revision_reclamo(request,id):
    reclamo = get_object_or_404(Reclamo, id=id)
    form = ActualizarEstadoReclamoForm(instance=reclamo)
    
    if request.method == 'POST':
        form = ActualizarEstadoReclamoForm(request.POST, instance=reclamo)
        if form.is_valid():
            form.save()
            return redirect('revision_reclamo', id=reclamo.id)
    
    datos = {
        "reclamo": reclamo,
        "form":form
    }
    
    return render(request,'vet/revision_reclamo.html' ,datos)
    
    

