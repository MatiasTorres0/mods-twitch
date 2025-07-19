from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Comando, Moderador, Anuncios, Notas_Mods, Stream_WWE, Combate_WWE  # Añadido Anuncios


class ModeradorRegistroForm(UserCreationForm):
    class Meta:
        model = Moderador
        fields = ['nombre_twitch', 'alias', 'email', 'password1', 'password2']
        
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

class ComandoForm(forms.ModelForm):
    class Meta:
        model = Comando
        fields = ['nombre_comando', 'tipo_comando', 'descripcion', 'activo', 'ejemplo']
        widgets = {
            'nombre_comando': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: !saludo'}),
            'tipo_comando': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción breve del comando', 'maxlength': '1000'}),
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
        
        # Actualizar el widget para permitir 1000 caracteres
        if 'descripcion' in self.fields:
            self.fields['descripcion'].widget.attrs.update({'maxlength': '1000'})


class AnunciosForm(forms.ModelForm):
    class Meta:
        model = Anuncios
        fields = ['titulo', 'contenido', 'fecha_inicio', 'fecha_fin', 'activo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha_inicio': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'fecha_fin': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulo'].label = "Título"
        self.fields['contenido'].label = "Contenido"
        self.fields['fecha_inicio'].label = "Fecha de Inicio"
        self.fields['fecha_fin'].label = "Fecha de Fin"
        self.fields['activo'].label = "¿Activo?"

class Notas_ModsForms(forms.ModelForm):
    class Meta:
        model = Notas_Mods
        fields = ['Titulo', 'contenido', 'categoria', 'prioridad']
        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'prioridad': forms.Select(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Titulo'].label = "Título"
        self.fields['contenido'].label = "Contenido"
        self.fields['categoria'].label = "Categoría"
        self.fields['prioridad'].label = "Prioridad"

class Stream_WWEForms(forms.ModelForm):
    class Meta:
        model = Stream_WWE
        fields = ['fecha_stream']
        widgets = {
            'fecha_stream': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_stream'].label = "Fecha del Stream"

class Combate_WWEForms(forms.ModelForm):
    class Meta:
        model = Combate_WWE
        fields = ['stream', 'luchador_1', 'luchador_2', 'resultado', 'orden_combate']
        widgets = {
            'stream': forms.Select(attrs={'class': 'form-control'}),
            'luchador_1': forms.TextInput(attrs={'class': 'form-control'}),
            'luchador_2': forms.TextInput(attrs={'class': 'form-control'}),
            'resultado': forms.Select(attrs={'class': 'form-control'}),
            'orden_combate': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stream'].label = "Stream"
        self.fields['luchador_1'].label = "Luchador 1"
        self.fields['luchador_2'].label = "Luchador 2"
        self.fields['resultado'].label = "Resultado"
        self.fields['orden_combate'].label = "Orden del Combate"