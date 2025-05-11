from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Moderador

class ModeradorRegistroForm(UserCreationForm):
    class Meta:
        model = Moderador
        fields = ['nombre_twitch', 'alias', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_twitch'].label = "Nombre de Twitch"
        self.fields['alias'].label = "Alias (nombre visible)"
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
        
        # Filtrar nombres de Twitch ya utilizados
        nombres_usados = Moderador.objects.values_list('nombre_twitch', flat=True)
        opciones_disponibles = [(key, value) for key, value in Moderador.MODERADOR if key not in nombres_usados]
        self.fields['nombre_twitch'].choices = [('', 'Selecciona tu nombre de Twitch')] + opciones_disponibles