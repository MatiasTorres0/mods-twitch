from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate # Import login as auth_login globally
from django.contrib import messages  # Asegúrate de importar messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ModeradorRegistroForm
from .models import Moderador

class ModeradorRegistroView(CreateView):
    model = Moderador
    form_class = ModeradorRegistroForm
    template_name = 'core/registro.html'
    success_url = reverse_lazy('login')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrar nombres de Twitch ya utilizados
        nombres_usados = Moderador.objects.values_list('nombre_twitch', flat=True)
        opciones_disponibles = [(key, value) for key, value in Moderador.MODERADOR if key not in nombres_usados]
        form.fields['nombre_twitch'].choices = [('', 'Selecciona tu nombre de Twitch')] + opciones_disponibles
        return form
    
    def form_valid(self, form):
        # Guardar el usuario primero
        user = form.save()
        
        try:
            # Autenticar y loguear al usuario después del registro
            username = form.cleaned_data.get('nombre_twitch')
            password = form.cleaned_data.get('password1')
            
            # Usar authenticate con el nombre de usuario correcto
            # Cambio aquí: usar nombre_twitch en lugar de username
            user_auth = authenticate(self.request, nombre_twitch=username, password=password)
            
            if user_auth is not None:
                auth_login(self.request, user_auth)  # Usar auth_login
            else:
                # Si la autenticación falla, registrar el error pero continuar
                print(f"Error de autenticación para el usuario {username}")
        except Exception as e:
            # Capturar cualquier excepción durante la autenticación
            print(f"Error durante la autenticación: {str(e)}")
        
        # Siempre redirigir al usuario, incluso si la autenticación falla
        return super().form_valid(form)

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def service(request):
    return render(request, 'core/service.html')

def blog(request):
    return render(request, 'core/blog.html')

def blog_details(request):
    return render(request, 'core/blog_details.html')

def registro(request):
    if request.method == 'POST':
        form = ModeradorRegistroForm(request.POST)
        print("Formulario enviado")
        print("Errores:", form.errors)
        if form.is_valid():
            user_obj = form.save() # Renamed to user_obj to avoid conflict with user variable below
            nombre_twitch = form.cleaned_data.get('nombre_twitch')
            password = form.cleaned_data.get('password1')
            # Authenticate the user that was just created
            # Cambio aquí: usar nombre_twitch en lugar de username
            user_auth = authenticate(request, nombre_twitch=nombre_twitch, password=password)
            # En la función registro o en ModeradorRegistroView
            if user_auth is not None:
                auth_login(request, user_auth)
                messages.success(request, f'¡Registro exitoso! Recuerda que tu nombre de usuario para iniciar sesión es: {nombre_twitch}')
                return redirect('login')
            else:
                # This case might happen if password hashing or username field is mismatched
                messages.error(request, "No se pudo autenticar después del registro.")
                return redirect('login')
    else:
        form = ModeradorRegistroForm()
    return render(request, 'registro/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') # 'username' aquí es el valor del campo nombre_twitch del formulario
        password = request.POST.get('password')
        
        # Intentar autenticar con el nombre exacto
        user = authenticate(request, nombre_twitch=username, password=password)
        
        # Si falla, intentar buscar el usuario manualmente para dar un mensaje más específico
        if user is None:
            try:
                # Verificar si existe un moderador con ese nombre (ignorando mayúsculas/minúsculas)
                posible_moderador = Moderador.objects.filter(nombre_twitch__iexact=username).first()
                if posible_moderador:
                    # Existe el usuario pero la contraseña es incorrecta
                    messages.error(request, 'Contraseña incorrecta. Por favor, intenta de nuevo.')
                else:
                    # No existe un usuario con ese nombre
                    messages.error(request, f'No existe un moderador con el nombre "{username}". Verifica que sea tu nombre de Twitch exacto.')
            except:
                # Error general
                messages.error(request, 'Nombre de Twitch o contraseña incorrectos.')
            return render(request, 'registro/login.html', {'error_message': 'Credenciales incorrectas'})
        
        # Si la autenticación es exitosa
        auth_login(request, user)
        return redirect('inicio')
    
    return render(request, 'registro/login.html')

def inicio(request):
    return render(request, 'dashboard/inicio.html')

def comandos(request):
    return render(request, 'dashboard/comandos.html')

def protocolos(request):
    return render(request, 'dashboard/protocolos.html')

def anuncios(request):
    return render(request, 'dashboard/anuncios.html')