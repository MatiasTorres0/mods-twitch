from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
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
        response = super().form_valid(form)
        # Autenticar y loguear al usuario después del registro
        username = form.cleaned_data.get('nombre_twitch')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response

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
    return render(request, 'core/registro.html')

def login(request):
    return render(request, 'core/login.html')