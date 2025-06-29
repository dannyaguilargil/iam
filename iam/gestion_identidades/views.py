from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import solicitud, respuestasolicitud
from .utils import generar_formulario_dinamico 
from django.contrib.auth.models import User
from django.core.mail import send_mail
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.groups.filter(name='usuario').exists():
                    login(request, user)
                    return redirect('test')
                elif user.is_staff:
                    login(request, user)
                    return redirect('/admin')
                else:
                    login(request, user)
                    #messages.error(request, 'No tiene permisos asociados, contacte al amdinistrador.')
                    return redirect('test')
                   
                   
        else:
            print("Usuario invalido")
            messages.error(request, 'Ingresar credenciales validos para iniciar sesión.')
            return redirect('inicio')
    else:
        print("Renderizado")
        #messages.error(request, 'Las credenciales de inicio de sesión son inválidas.')
        form = AuthenticationForm()

    return render(request, 'home.html', {'form': form})


def registro_usuario(request):
    form_def = get_object_or_404(solicitud, tipo='creacion_usuario')
    FormClass = generar_formulario_dinamico(form_def.estructura_json)

    if request.method == "POST":
        form = FormClass(request.POST)
        if form.is_valid():
            datos = form.cleaned_data

            # Guardar la respuesta del formulario
            respuestasolicitud.objects.create(
                solicitud=form_def,
                datos=datos
            )

            username = datos.get("usuario")
            password = datos.get("password")
            email = datos.get("email")
            nombre = datos.get("nombre")
            apellido = datos.get("apellidos")

            if User.objects.filter(username=username).exists():
                messages.error(request, "Ese nombre de usuario ya existe.")
            else:
                usuario = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=nombre,
                    last_name=apellido
                )

                # Envío de correo de bienvenida
                mensaje = f"""
                Hola {nombre},

                Tu cuenta ha sido creada exitosamente en el sistema IAM.

                Tus credenciales de acceso son:

                Usuario: {username}
                Contraseña: {password}

                Por favor, inicia sesión en el sistema y cambia tu contraseña después del primer ingreso.

                Saludos,
                Equipo IAM
                """
                try:
                    send_mail(
                        subject='Cuenta creada - IAM',
                        message=mensaje,
                        from_email='noreply@dannyhub.com', 
                        recipient_list=[email],
                        fail_silently=False
                    )
                    messages.success(request, "Usuario creado correctamente. Se ha enviado un correo con los datos de acceso.")
                except Exception as e:
                    print(f"Error enviando correo: {e}")  
                    messages.warning(request, f"Usuario creado pero no se pudo enviar el correo: {e}")

                return redirect('login')

    else:
        form = FormClass()

    return render(request, 'responder_formulario.html', {
        'solicitud': form_def,
        'form': form
    })