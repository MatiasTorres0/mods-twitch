from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Comando, Moderador

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

class ComandoForm(forms.ModelForm): # Cambiado de forms.Form a forms.ModelForm
    class Meta:
        model = Comando
        fields = ['nombre_comando', 'tipo_comando', 'descripcion', 'activo', 'ejemplo']
        widgets = {
            'nombre_comando': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: !saludo'}),
            'tipo_comando': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción breve del comando'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ejemplo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: !saludo @usuario'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Puedes personalizar etiquetas aquí si es necesario, por ejemplo:
        self.fields['nombre_comando'].label = "Nombre del Comando"
        self.fields['tipo_comando'].label = "Tipo de Comando"
        self.fields['descripcion'].label = "Descripción"
        self.fields['activo'].label = "Activo"
        self.fields['ejemplo'].label = "Ejemplo de Uso"