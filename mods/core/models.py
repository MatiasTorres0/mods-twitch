from email.policy import default
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
# Create your models here.
class Comando(models.Model):
    TIPO_COMANDO = (
        ('EVERYONE', 'Everyone'),
        ('VIP', 'VIP'),
        ('MODERATOR', 'Moderator'),
        ('SUPER_MODERATOR', 'Super Moderator'),
    )
    ACTIVO = (
        (True, 'Activo'),
        (False, 'Inactivo'),
    )
    nombre_comando = models.CharField(max_length=20, unique=True)
    tipo_comando = models.CharField(max_length=20, choices=TIPO_COMANDO, default='TODOS')
    descripcion = models.CharField(max_length=1000)
    activo = models.BooleanField(default=True, choices=ACTIVO)
    ejemplo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_comando

class ModeradorManager(BaseUserManager):
    def create_user(self, nombre_twitch, alias, password=None):
        if not nombre_twitch:
            raise ValueError('El moderador debe tener un nombre de Twitch')
        
        user = self.model(
            nombre_twitch=nombre_twitch,
            alias=alias,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, nombre_twitch, alias, password=None):
        user = self.create_user(
            nombre_twitch=nombre_twitch,
            alias=alias,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Moderador(AbstractUser):
    MODERADOR = (
        ('ELCILANTROUWU', 'elcilantrouwu'),
        ('JOSHUAKOMODO', 'joshuakomodo'),
        ('KEDOP_19', 'kedop_19'),
        ('MELODYZOMBIE', 'MelodyZombie'),
        ('MRPONCHO345', 'mrponcho345'),
        ('POIYUTE', 'PoiYuTe'),
        ('CHACHOYVT', 'ChachoyVT'),
    )
    
    # Eliminar campos heredados que no necesitamos
    username = None
    first_name = None
    last_name = None
    
    # Nuevos campos
    nombre_twitch = models.CharField(max_length=20, choices=MODERADOR, unique=True)
    alias = models.CharField(max_length=30, unique=True, default='')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=128, default='changeme')
    # Configuración para autenticación
    USERNAME_FIELD = 'nombre_twitch'
    # En la clase Moderador, agregar:
    email = models.EmailField(unique=True)
    # Actualizar REQUIRED_FIELDS
    REQUIRED_FIELDS = ['alias', 'email']
    
    objects = ModeradorManager()
    
    def __str__(self):
        return self.alias
    
    def clean(self):
        # Verificar si este es un objeto existente (ya tiene ID)
        if self.pk:
            # Obtener el objeto original de la base de datos
            original = Moderador.objects.get(pk=self.pk)
            # Si el nombre de Twitch ha cambiado, lanzar error
            if original.nombre_twitch != self.nombre_twitch:
                raise ValidationError('El nombre de Twitch no puede ser modificado después de la creación.')
        super().clean()

class Anuncios(models.Model):
    titulo = models.CharField(max_length=100, default="")
    contenido = models.TextField(max_length=20000, default="")
    fecha_inicio = models.DateTimeField(default=timezone.now)
    fecha_fin = models.DateTimeField(default=timezone.now)
    activo = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    mensaje = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mensaje

class Notas_Mods(models.Model):
    CATEGORIA = (
        ('SUGERENCIAS', 'SUGERENCIAS'),
        ('BUGS', 'BUGS'),
        ('OTROS', 'OTROS'),
    )
    PRIORIDAD = (
        ('ALTA', 'ALTA'),
        ('MEDIA', 'MEDIA'),
        ('BAJA', 'BAJA'),
    )
    Titulo = models.CharField(max_length=150)
    contenido = models.CharField(max_length=20000)
    categoria = models.CharField(max_length=100, choices=CATEGORIA, default='OTROS')
    prioridad = models.CharField(max_length=100, choices=PRIORIDAD, default='BAJA')
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Titulo

class Stream_WWE(models.Model):
    fecha_stream = models.DateTimeField()
    
    def __str__(self):
        return f"Stream WWE {self.fecha_stream.strftime('%Y-%m-%d')}"

class Combate_WWE(models.Model):
    TIPO_COMBATE = (
        ('INDIVIDUAL', 'Individual'),
        ('PAREJAS', 'Parejas'),
        ('ESPECIAL', 'Especial'),
    )
    
    RESULTADOS = (
        ('VICTORIA', 'Victoria'),
        ('DERROTA', 'Derrota'),
        ('EMPATE', 'Empate'),
        ('NO_CONTEST', 'Sin Decisión'),
    )
    
    stream = models.ForeignKey(Stream_WWE, on_delete=models.CASCADE, related_name='combates')
    tipo_combate = models.CharField(max_length=20, choices=TIPO_COMBATE, default='INDIVIDUAL')  # Nuevo campo
    luchador_1 = models.CharField(max_length=100, blank=True, null=True)
    luchador_2 = models.CharField(max_length=100, blank=True, null=True)
    luchador_3 = models.CharField(max_length=100, blank=True, null=True)  # Nuevo campo
    luchador_4 = models.CharField(max_length=100, blank=True, null=True)  # Nuevo campo
    resultado = models.CharField(max_length=20, choices=RESULTADOS, default='NO_CONTEST')
    orden_combate = models.PositiveIntegerField(help_text="Orden del combate en el stream")
    
    class Meta:
        ordering = ['stream', 'orden_combate']
    
    def __str__(self):
        if self.tipo_combate == 'PAREJAS':
            return f"{self.luchador_1} & {self.luchador_2} vs {self.luchador_3} & {self.luchador_4}"
        elif self.tipo_combate == 'ESPECIAL':
            return f"Evento Especial: {self.luchador_1}"
        else:
            return f"{self.luchador_1} vs {self.luchador_2}"