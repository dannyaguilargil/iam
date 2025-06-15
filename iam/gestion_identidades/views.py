from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

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
                    messages.error(request, 'No tiene permisos asociados, contacte al amdinistrador.')
                    return redirect('inicio')
                   
                   
        else:
            print("Usuario invalido")
            messages.error(request, 'Ingresar credenciales validos para iniciar sesión.')
            return redirect('inicio')
    else:
        print("Renderizado")
        #messages.error(request, 'Las credenciales de inicio de sesión son inválidas.')
        form = AuthenticationForm()

    return render(request, 'home.html', {'form': form})
