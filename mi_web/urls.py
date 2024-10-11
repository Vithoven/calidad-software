"""
URL configuration for sitio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path , include
from . import views  

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',views.index,name='index'),
    path('carrito_login/',views.carrito_login,name='carrito_login'),
    
    path('lista_compras/',views.lista_compras,name='lista_compras'),
    
    path('recordando/',views.recordando,name='recordando'),
    
    path('Revision_estado/<id>',views.Revision_estado,name='Revision_estado'),
    
    path('tienda_trabajador/',views.tienda_trabajador,name='tienda_trabajador'),
    path('trabajador/',views.trabajador,name='trabajador'),
    path('usuarios_admin/',views.usuarios_admin,name='usuarios_admin'),
    
    path('login/',views.login_xd,name='login'),
    path('detalleP_trabajador/<id>',views.detalleP_trabajador,name='detalleP_trabajador'),
    path('eliminarP_trabajador/<id>',views.eliminarP_trabajador,name='eliminarP_trabajador'),
    path('cerrar/',views.cerrar,name='cerrar'),
    
    path('registro/',views.registro,name='registro'),
    path('mi_cuenta/<id>',login_required(views.mi_cuenta),name='mi_cuenta'),
    
    path('mi_cuenta_td/<id>/<usuario>',views.mi_cuenta_td,name='mi_cuenta_td'),
    
    path('ver_carrito/', login_required(views.ver_carrito), name='ver_carrito'),
    
    path('agregar_producto/<int:producto_id>/', views.agregar_producto,name='agregar_producto'),
    
    path('eliminar/<int:item_id>/', views.eliminar_producto, name='eliminar_producto'),

    path('detalle_producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    
    path('ver_boleta/<id>',login_required(views.ver_boleta),name='ver_boleta'),
    path('', include('django.contrib.auth.urls')),  # Incluir URLs de autenticación

    path('bloqueo_admin/<id>',views.bloqueo_admin,name='bloqueo_admin'),
    path('desbloqueo_admin/<id>',views.desbloqueo_admin,name='desbloqueo_admin'),
    
    path('Crear_reclamo/<id>', views.Crear_reclamo, name='Crear_reclamo'),
    path('reclamos_admin/', views.reclamos_admin, name='reclamos_admin'),
    path('revision_reclamo/<id>', views.revision_reclamo, name='revision_reclamo'),
    
    
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
