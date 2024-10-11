from typing import Any
from django import forms
from .models import producto , Tarjeta , ItemCarrito , Boleta ,Bloqueo ,Desbloqueo,Reclamo , Usuario ,Provincia, Comuna
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm ,UserChangeForm ,PasswordChangeForm
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout , Submit , Div ,Field ,HTML,Row,Column
from crispy_forms.bootstrap import PrependedText
from .enumeraciones import *
  
useru = get_user_model()
class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['nombre','stock','descripción','precio','foto']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].widget.attrs.update({'id': 'stock_id'})
        self.fields['precio'].widget.attrs.update({'id': 'precio_id'})
         
         
class upProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['nombre','stock','descripción','precio','foto']  
         
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'id': 'nombre_id'})
        self.fields['stock'].widget.attrs.update({'id': 'stock_id'})
        self.fields['descripción'].widget.attrs.update({'id': 'descripción_id'})  # Corrige 'descripción' a 'descripcion' si no tiene acento en el modelo
        self.fields['precio'].widget.attrs.update({'id': 'precio_id'})
        self.fields['foto'].widget.attrs.update({'id': 'foto_id'})
        
class loginForm(AuthenticationForm):
    pass


class createUser(UserCreationForm):
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), empty_label="Selecciona comuna")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"id":"password1"}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={"id":"password2"}))
    
    class Meta:
        model = useru 
        fields =["correo","run","nombre","apellido","telefono","comuna","direccion"]

    def __init__(self, *args , **kwargs ):
        super().__init__(*args, **kwargs)
        self.helper= FormHelper()
        self.helper.form_method="post"
        self.helper.form_class="needs-validation"
        self.helper.attrs={"novalidate":""}
        self.helper.layout=Layout(
           Field("correo",id="correo") ,
           Field("run",id="Rut") ,
           Field("nombre",id="nombre"), 
           Field("apellido",id="apellido"), 
           Div(
                Div(
                    PrependedText('telefono', '+56', active=True , id="fono"),
                    css_class='input-group'
                ,id="fono2"),
                css_class='form-group'
            ),
           Field("comuna",id="comuna"), 
           Field("direccion",id="direc"), 
           Field("password1",id="contraseña"), 
           Field("password2",id="repetirContraseña")    
        )
            
        
class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ["tarjeta_de_credito", "fecha_de_vencimiento", "codigo_de_seguridad"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper= FormHelper()
        self.helper.form_method="post"
        self.helper.form_class="needs-validation"
        self.helper.attrs={"novalidate":""}
        self.fields['tarjeta_de_credito'].widget.attrs.update({'id': 'tarjeta'})
        self.fields['fecha_de_vencimiento'].widget.attrs.update({'id': 'fecha'})
        self.fields['codigo_de_seguridad'].widget.attrs.update({'id': 'cs'})

class UpdateTarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ["tarjeta_de_credito", "fecha_de_vencimiento", "codigo_de_seguridad"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "needs-validation"
        self.helper.attrs = {"novalidate": ""}
        self.helper.layout = Layout(
            Field('tarjeta_de_credito', css_class='form-control', id='tarjeta'),
            Field('fecha_de_vencimiento', css_class='form-control', id='fecha'),
            Field('codigo_de_seguridad', css_class='form-control', id='cs'),
            
        )

        # Custom attributes for fields
        self.fields['tarjeta_de_credito'].widget.attrs.update({'id': 'tarjeta'})
        self.fields['tarjeta_de_credito'].widget.attrs['readonly'] = True
        self.fields['fecha_de_vencimiento'].widget.attrs.update({'id': 'fecha'})
        self.fields['codigo_de_seguridad'].widget.attrs.update({'id': 'cs'})
        
class updateUser(UserChangeForm):
    
    class Meta:
        model = useru 
        fields =["nombre","apellido","telefono","comuna","direccion"]
        
    def __init__(self, *args , **kwargs ):
        super().__init__(*args, **kwargs)
        
        self.helper= FormHelper()
        self.helper.form_method="post"
        self.helper.form_class="needs-validation"
        self.helper.attrs={"novalidate":""}
        self.helper.layout=Layout(
           Field("nombre",id="nombre"), 
           Field("apellido",id="apellido"), 
           Div(
                Div(
                    PrependedText('telefono', '+56', active=True , id="fono"),
                    css_class='input-group'
                ,id="fono2"),
                css_class='form-group'
            ),
           Field("comuna",id="comuna"), 
           Field("direccion",id="direc") 
        )
        # Elimina los campos de contraseña ya que no se necesitan para actualizar el perfil
        if 'password' in self.fields:
            del self.fields['password']
        # Establecer el valor actual del usuario para el campo comuna
        
class upPassUser(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'needs-validation'
        self.helper.attrs = {'novalidate': ''}
        self.helper.layout = Layout(
            Field('old_password', id='old_password'),
            Field('new_password1', id='contraseña'),
            Field('new_password2', id='repetirContraseña')
        )

class ItemCarritoForm(forms.ModelForm):
    class Meta:
        model = ItemCarrito
        fields = ['cantidad']



class BoletaForm(forms.ModelForm):
    
    comuna2 = forms.ModelChoiceField(queryset=Comuna.objects.all(), empty_label="Selecciona comuna")

    class Meta:
        model = Boleta
        fields = ['metodoDePago', 'telefono2', 'comuna2', 'direccion2', 'rut_receptor', 'nombre_receptor']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['metodoDePago'].queryset = Tarjeta.objects.filter(uusuario=user)

        self.fields['metodoDePago'].label = "Método de Pago"
        
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "needs-validation"
        self.helper.attrs = {"novalidate": ""}
        
        self.helper.layout = Layout(
            HTML('<h3>Datos de pago</h3>'),
            Field("metodoDePago", id="metodoDePago"),
            HTML('<h3>Datos de dirección y método de contacto</h3>'),
            Field("comuna2", id="comuna"),
            Field("direccion2", id="direc"),
            Field("telefono2", id="fono"),
            HTML('<h3>Datos del Receptor</h3>'),
            Field("rut_receptor", id="Rut"),
            Field("nombre_receptor", id="nombre"),
            Submit('submit', 'Pagar', css_class='btn btn-primary')
        )
        
        self.fields['telefono2'].widget.attrs.update({'id': 'fono'})
        self.fields['direccion2'].widget.attrs.update({'id': 'direc'})
        self.fields['rut_receptor'].widget.attrs.update({'id': 'Rut'})
        self.fields['nombre_receptor'].widget.attrs.update({'id': 'nombre'})
        
class UsuarioFilterForm(forms.Form):
    nombre = forms.CharField(required=False, label='Nombre')
    apellido = forms.CharField(required=False, label='Apellido')
    es_baneado = forms.BooleanField(required=False, label='Es baneado', initial=False)
    
    
class BloqueoForm(forms.ModelForm):
    class Meta:
        model = Bloqueo
        fields = ['razon']
        
class DesbloqueoForm(forms.ModelForm):
    class Meta:
        model = Desbloqueo
        fields = ['razon']
        
class BoletaFilterForm(forms.Form):
    ESTADO_SIN_FILTRO = [('', 'Sin Filtro')] + list(ESTADO_ENVIO)
    
    estado = forms.ChoiceField(label='Estado', choices=ESTADO_SIN_FILTRO ,required=False, initial='')
    
    def __init__(self, *args, **kwargs):
        super(BoletaFilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.add_input(Submit('submit', 'Filtrar'))
        
    def filter_queryset(self, queryset):
        estado = self.cleaned_data.get('estado')

        if estado:
            queryset = queryset.filter(estado=estado)
        
        return queryset
    
class ProductoFilterForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50, required=False)
    precio_min = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    precio_max = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        super(ProductoFilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.layout = Layout(
            Row(
                Column('nombre', css_class='form-group mb-0'),
                css_class='form-row'
            ),
            Row(
                Column(
                    HTML("""
                        <label for="priceRange" class="form-label">Rango de Precio</label>
                        <input type="range" class="form-range" id="priceRange" min="0" max="150000" step="1000">
                        <p>Precio: <span id="priceMin">0</span> - <span id="priceMax">150000</span></p>
                    """),
                    css_class='form-group col-md-12 mb-0'
                ),
                css_class='form-row'
            ),
            'precio_min',
            'precio_max',
            Submit('submit', 'Filtrar', css_class='btn btn-primary mt-2')
        )

    def filter_queryset(self, queryset):
        nombre = self.cleaned_data.get('nombre')
        precio_min = self.cleaned_data.get('precio_min')
        precio_max = self.cleaned_data.get('precio_max')
        
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if precio_min is not None:
            queryset = queryset.filter(precio__gte=precio_min)
        if precio_max is not None:
            queryset = queryset.filter(precio__lte=precio_max)
        
        return queryset

class ActualizarEstadoBoletaForm(forms.ModelForm):
    class Meta:
        model = Boleta
        fields = ['estado']


class ReclamoForm(forms.ModelForm):
    class Meta:
        model = Reclamo
        fields = ['tipo', 'descripcion']
        labels = {
            'tipo': 'Tipo de reclamo',
            'descripcion': 'Descripción del reclamo',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }


class ReclamoFilterForm(forms.Form):
    ESTADO_Reclamo_SIN_FILTRO = [('', 'Sin Filtro')] + list(ESTADOS_RECLAMO)
    usuarios = forms.ModelChoiceField(queryset=Usuario.objects.all(), label='Usuario', required=False)
    boletas = forms.ModelChoiceField(queryset=Boleta.objects.all(), label='Boleta', required=False)
    estado = forms.ChoiceField(choices=ESTADO_Reclamo_SIN_FILTRO, label='Estado', required=False,initial='')
    
class ActualizarEstadoReclamoForm(forms.ModelForm):
    class Meta:
        model = Reclamo
        fields = ['estado']