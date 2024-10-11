$("#correo").after("<div id='mensajeErrorCorreoCrear'></div>");
$("#Rut").after("<div id='mensajeErrorRut'></div>");
$("#contraseña").after("<div id='mensajeErrorContraseña'></div>");
$("#repetirContraseña").after("<div id='mensajeErrorRepetirContraseña'></div>");
$("#nombre").after("<div id='mensajeErrorNombre'></div>");
$("#apellido").after("<div id='mensajeErrorApellido'></div>");
$("#fono2").after("<div id='mensajeErrorTelefono'></div>");
$("#comuna").after("<div id='mensajeErrorComuna'></div>");
$("#direc").after("<div id='mensajeErrorDirec'></div>");

$("#tarjeta").after("<div id='mensajeErrortarjeta'></div>");
$("#fecha").after("<div id='mensajeErrorfecha'></div>");
$("#cs").after("<div id='mensajeErrorcs'></div>");


$("#correo").on("input", validarCorreoCrear);
$("#contraseña").on("input", contra_1);
$("#repetirContraseña").on("input", contra_2);
$("#nombre").on("input", nombre_v);
$("#apellido").on("input", apellido_v);
$("#comuna").on("input", comuna);
$("#direc").on("input", direc);
$("#fono").on("input", telefono);

$("#tarjeta").on("input", tageta_v);
$("#fecha").on("input", vencimiento_v);
$("#cs").on("input", codigo_v);

$("#Rut").on("input", function () {
    formatRut();
    validaRut();
});

$("#tarjeta").on("keypress", function (event) {
    return soloNumeros(event);
});

$("#fono").on("keypress", function (event) {
    return soloNumeros(event);
});

$("#fecha").on("keypress", function (event) {
    return soloNumeros(event);
});

$("#cs").on("keypress", function (event) {
    return soloNumeros(event);
});

$("#stock_id").on("keypress", function (event) {
    return soloNumeros(event);
});

$("#precio_id").on("keypress", function (event) {
    return soloNumeros(event);
});

function validarCorreoCrear() {
    var coreoinp = document.getElementById("correo");
    var correo = document.getElementById("correo").value;
    var mensajeError = document.getElementById("mensajeErrorCorreoCrear");

    if (correo === "") {
        mensajeError.innerText = "Por favor, ingrese su correo.";
        mensajeError.style.color = "red";
        coreoinp.setCustomValidity("no valido");
        return false; // Evita que se envíe el formulario si el correo está vacío
    }else if (correo.includes("@trabajador.com")) {
        mensajeError.innerText = "Correo electrónico de trabajador válido ✅";
        mensajeError.style.color = "green";
        coreoinp.setCustomValidity("");
        return true; // Envía el formulario si el correo contiene "@trabajador.com"
    }else if (correo.includes("@gmail.com") || correo.includes("@hotmail.com")) {
        mensajeError.innerText = "Correo electrónico válido ✅";
        mensajeError.style.color = "green"; 
        coreoinp.setCustomValidity("");
        return true; // correo valido
    }else if (correo.includes("@gmail.cl") || correo.includes("@hotmail.cl")) {
        mensajeError.innerText = "Correo electrónico válido ✅";
        mensajeError.style.color = "green"; 
        coreoinp.setCustomValidity("");
        return true; // correo valido
    }else {
        mensajeError.innerText = "Ingrese un correo válido.";
        mensajeError.style.color = "red";
        coreoinp.setCustomValidity("no valido");
        return false; // Evita que se envíe el formulario si el correo no contiene "@gmail o @hotmail .com o .cl" 
    }
}
// Valida el rut con su cadena completa "XXXXXXXX-X"
function validaRut() {
    var rutinp = document.getElementById("Rut");
    var rutCompleto = document.getElementById("Rut").value;
    var mensajeError = document.getElementById("mensajeErrorRut");

    if (rutCompleto === "") {
        mensajeError.innerText = "Por favor, ingrese su run ";
        mensajeError.style.color = "red";
        rutinp.setCustomValidity("no");
        return false;
    }else if (/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rutCompleto)){
        var tmp = rutCompleto.split('-');
        var digv = tmp[1];
        var rut = tmp[0];
        if (digv == 'K') {
            digv = 'k';
        }
        
        if (dv(rut) == digv){
            mensajeError.innerText = "Run válido ✅";
            mensajeError.style.color = "green";
            rutinp.setCustomValidity("");
            return true;
        }else {
            mensajeError.innerText = "Por favor, ingrese un run válido ";
            mensajeError.style.color = "red";
            rutinp.setCustomValidity("no");
            return false;
        }    
    }else {
        mensajeError.innerText = "Por favor, ingrese un run válido ";
        mensajeError.style.color = "red";
        rutinp.setCustomValidity("no");
        return false;
    }   
}
function dv(T) {
    var M = 0, S = 1;
    for (; T; T = Math.floor(T / 10))
        S = (S + T % 10 * (9 - M++ % 6)) % 11;
    return S ? S - 1 : 'k';
}
function formatRut() {
    let rutInput = document.getElementById("Rut");
    let rut = rutInput.value.replace(/[^\dkK]/g, ''); // Elimina cualquier caracter que no sea un dígito o 'k' (mayúscula o minúscula)
    rut = rut.replace(/^0+/, ''); // Elimina ceros a la izquierda
    
    let formattedRut = '';
    let rutLength = rut.length;
    
    if (rutLength > 1) {
        for (let i = 0; i < rutLength - 1; i++) {
            formattedRut += rut.charAt(i);
            if (i === rutLength - 2) {
                formattedRut += '-';
            }
        }
        formattedRut += rut.charAt(rutLength - 1);
    } else {
        formattedRut = rut;
    }
    
    rutInput.value = formattedRut;
}
function contra_1() {
    var contraseña = document.getElementById("contraseña").value;
    var mensajeError = document.getElementById("mensajeErrorContraseña");
    var coninp = document.getElementById("contraseña");

    // Expresiones regulares para validar la contraseña
    var tieneNumero = /[0-9]/.test(contraseña);
    var tieneMayuscula = /[A-Z]/.test(contraseña);
    var tieneCaracterEspecial = /[.!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\-]/.test(contraseña);

    if (contraseña === "") {
        mensajeError.innerText = "Por favor, ingrese una contraseña";
        mensajeError.style.color = "red";
        coninp.setCustomValidity("no");
        return false;
    } else if (contraseña.length < 8) {
        mensajeError.innerText = "La contraseña debe tener al menos 8 caracteres";
        mensajeError.style.color = "red";
        coninp.setCustomValidity("no");
        return false;
    } else if (!tieneNumero || !tieneMayuscula || !tieneCaracterEspecial) {
        mensajeError.innerText = "La contraseña debe incluir al menos un número, una mayúscula y un carácter especial (como .!@#$%^&*)";
        mensajeError.style.color = "red";
        coninp.setCustomValidity("no");
        return false;
    } else {
        mensajeError.innerText = "Contraseña ingresada correctamente ✅";
        mensajeError.style.color = "green";
        coninp.setCustomValidity("");
        return true;
    }
}
function contra_2() {
    var con2inp = document.getElementById("repetirContraseña");
    var contraseña = document.getElementById("contraseña").value;
    var repetirContraseña = document.getElementById("repetirContraseña").value; // Obtener el valor del campo de repetir contraseña
    var mensajeError = document.getElementById("mensajeErrorRepetirContraseña");

    if (contraseña === "") {
        mensajeError.innerText = "Por favor, ingrese una contraseña";
        mensajeError.style.color = "red";
        con2inp.setCustomValidity("no");
        return false;
    } else if (contraseña.length < 6) {
        mensajeError.innerText = "La contraseña debe tener al menos 6 caracteres";
        mensajeError.style.color = "red";
        con2inp.setCustomValidity("no");
        return false;// Evita que se envíe el formulario si la contraseña tiene menos de 6 caracteres
    }else if (repetirContraseña !== contraseña) {
        mensajeError.innerText = "Las contraseñas no coinciden.";
        mensajeError.style.color = "red";
        con2inp.setCustomValidity("no");
        return false;
    } else {
        mensajeError.innerText = "Contraseñas iguales ✅";
        mensajeError.style.color = "green";
        con2inp.setCustomValidity("");
        return true;
    }
    
}
function nombre_v() {
    var nombinp = document.getElementById("nombre");
    var nombre = document.getElementById("nombre").value;
    var mensajeError = document.getElementById("mensajeErrorNombre");
    var regex = /^[a-zA-Z\s]+$/;

    if (nombre === "") {
        mensajeError.innerText = "Por favor, ingrese su nombre.";
        mensajeError.style.color = "red";
        nombinp.setCustomValidity("no");
        return false; // Evita que se envíe el formulario si el nombre está vacío
    } else if (!regex.test(nombre) || !nombre.replace(/\s/g, '').length) {
        mensajeError.innerText = "Por favor, ingrese un nombre valido.";
        mensajeError.style.color = "red";
        nombinp.setCustomValidity("no");
        return false;
    } else {
        mensajeError.innerText = "Nombre correcto ✅";
        mensajeError.style.color = "green";
        nombinp.setCustomValidity("");
        return true;
    }
}
function apellido_v() {
    var apeinp = document.getElementById("apellido");
    var apellido = document.getElementById("apellido").value;
    var mensajeError = document.getElementById("mensajeErrorApellido");
    var regex = /^[a-zA-Z\s]+$/;

    if (apellido === "") {
        mensajeError.innerText = "Por favor, ingrese su apellido.";
        mensajeError.style.color = "red";
        apeinp.setCustomValidity("no");
        return false; // Evita que se envíe el formulario si el apellido está vacío
    } else if (!regex.test(apellido) || !apellido.replace(/\s/g, '').length) {
        mensajeError.innerText = "Por favor, ingrese un apellido valido.";
        mensajeError.style.color = "red";
        apeinp.setCustomValidity("no");
        return false;
    }else {
        mensajeError.innerText = "Apellido correcto ✅";
        mensajeError.style.color = "green";
        apeinp.setCustomValidity("");
        return true;
    }
    
}
function telefono() {
    var fono2 = document.getElementById("fono");
    var telefono = document.getElementById("fono").value;
    var mensajeError = document.getElementById("mensajeErrorTelefono");

    if (telefono === "") {
        mensajeError.innerText = "Por favor, ingrese su número telefónico";
        mensajeError.style.color = "red";
        fono2.setCustomValidity("telefono no valido");
        return false;
    } else if (telefono.length !== 9) {
        mensajeError.innerText = "Por favor, ingrese un número válido";
        mensajeError.style.color = "red";
        fono2.setCustomValidity("telefono no valido");
        return false;
    } else {
        mensajeError.innerText = "Número válido ✅";
        mensajeError.style.color = "green";
        fono2.setCustomValidity("");
        return true;
    }
    
}
function comuna() {
    var comubinp = document.getElementById("comuna");
    var nombre = document.getElementById("comuna").value;
    var mensajeError = document.getElementById("mensajeErrorComuna");

    if (nombre === "") {
        mensajeError.innerText = "Por favor, ingrese una comuna.";
        mensajeError.style.color = "red";
        comubinp.setCustomValidity("no");
        return false; // Evita que se envíe el formulario si el nombre está vacío
    } else {
        mensajeError.innerText = "direccion correcta ✅";
        mensajeError.style.color = "green";
        comubinp.setCustomValidity("");
        return true;
    }
}
function direc() {
    var direcinp = document.getElementById("direc");
    var nombre = document.getElementById("direc").value;
    var mensajeError = document.getElementById("mensajeErrorDirec");

    if (nombre === "") {
        mensajeError.innerText = "Por favor, ingrese una direccion.";
        mensajeError.style.color = "red";
        direcinp.setCustomValidity("no");
        return false; // Evita que se envíe el formulario si el nombre está vacío
    } else {
        mensajeError.innerText = "direccion correcto ✅";
        mensajeError.style.color = "green";
        direcinp.setCustomValidity("");
        return true;
    }
}
function tageta_v() {
    var tarinp = document.getElementById("tarjeta");
    var numeroTarjeta = document.getElementById("tarjeta").value;
    var mensajeError = document.getElementById("mensajeErrortarjeta");

    if (numeroTarjeta === "") {
        mensajeError.innerText = "Por favor, ingrese su tarjeta.";
        mensajeError.style.color = "red";
        tarinp.setCustomValidity("no");
        return false;
    } else if (!/^[0-9]+$/.test(numeroTarjeta)) {
        mensajeError.innerText = "Por favor, no ingrese letras";
        mensajeError.style.color = "red";
        tarinp.setCustomValidity("no");
        return false;
    } else if (numeroTarjeta.length !== 16) {
        mensajeError.innerText = "Por favor, ingrese una tarjeta válida ";
        mensajeError.style.color = "red";
        tarinp.setCustomValidity("no");
        return false;
    } else {
        mensajeError.innerText = "Targeta válida ✅";
        mensajeError.style.color = "green";
        tarinp.setCustomValidity("");
        return true;
    }
    
}
function vencimiento_v() {
    var fechaups = document.getElementById("fecha");
    var fechaIngresada = document.getElementById("fecha").value;
    var mensajeError = document.getElementById("mensajeErrorfecha");

    // Obtiene el mes y el año actuales del sistema
    var fechaActual = new Date();
    var mesActual = fechaActual.getMonth() + 1; // Se suma 1 porque los meses van de 0 a 11
    var añoActual = fechaActual.getFullYear();

    // Expresión regular para validar el formato mes/año
    var regex = /^(0[1-9]|1[0-2])\/(\d{2})$/;

    // Validar si la fecha ingresada es válida
    if (fechaIngresada === "") {
        mensajeError.innerText = "Por favor, ingrese una fecha";
        mensajeError.style.color = "red";
        fechaups.setCustomValidity("no valido");
        return false;
    } else if (!regex.test(fechaIngresada)) {
        mensajeError.innerText = "Formato de fecha inválido. Debe ser mes/año (por ejemplo, 02/24)";
        mensajeError.style.color = "red";
        fechaups.setCustomValidity("no valido");
        return false;
    } else {
        // Obtener mes y año ingresados
        var partesFecha = fechaIngresada.split('/');
        var mesIngresado = parseInt(partesFecha[0], 10);
        var añoIngresado = 2000 + parseInt(partesFecha[1], 10); // Asumiendo que los años ingresados están en formato "YY" y los convertimos a "YYYY"

        // Comparar con la fecha actual
        if (añoIngresado < añoActual || (añoIngresado === añoActual && mesIngresado < mesActual)) {
            mensajeError.innerText = "Su tarjeta ya expiró, pruebe con otra.";
            mensajeError.style.color = "red";
            fechaups.setCustomValidity("no valido");
            return false; // Evita que se envíe el formulario
        } else {
            mensajeError.innerText = "Fecha válida ✅";
            mensajeError.style.color = "green";
            fechaups.setCustomValidity("");
            return true;
        }
    }
}

function codigo_v() {
    var feinp = document.getElementById("cs");
    var cs = document.getElementById("cs").value;
    var mensajeError = document.getElementById("mensajeErrorcs");

    if (cs === "") {
        mensajeError.innerText = "Por favor, ingrese una código de seguridad ";
        mensajeError.style.color = "red";
        feinp.setCustomValidity("no");
        return false;
    } else if (cs.length !== 3) {
        mensajeError.innerText = "Por favor, ingrese una código de seguridad válido";
        mensajeError.style.color = "red";
        feinp.setCustomValidity("no");
        return false;
    } else {
        mensajeError.innerText = "Código de seguridad válido ✅";
        mensajeError.style.color = "green";
        feinp.setCustomValidity("");
        return true;
    }
    
}

// Función para agregar la barra automáticamente después de ingresar el mes
document.getElementById('fecha').addEventListener('input', function (e) {
    var input = e.target;
    if (input.value.length === 2 && !input.value.includes('/')) {
        input.value += '/';
    }
});
document.getElementById('fecha').addEventListener('input', function (e) {
    var input = e.target;
    input.value = input.value.replace(/[^\d\/]|^\/$/g, ''); // Elimina cualquier carácter que no sea dígito o "/" y evita una barra solitaria al inicio
});

function soloNumeros(event) {
    var charCode = (event.which) ? event.which : event.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        event.preventDefault();
        return false;
    }
    return true;
}
// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }

            form.classList.add('was-validated')
        }, false)
    })
})()


function mostrarMensaje() {
    var mensajeError = document.createElement("span");
    mensajeError.textContent = "Producto agregado al carrito ✅";
    mensajeError.style.color = "green";
    
    // Insertar el mensaje después del botón "Agregar al carrito"
    var boton = document.getElementById("botonAgregar");
    boton.parentNode.insertBefore(mensajeError, boton.nextSibling);
    
    // Temporizador para que el mensaje desaparezca después de 4 segundos
    setTimeout(function() {
        mensajeError.remove();
    }, 4000);
}