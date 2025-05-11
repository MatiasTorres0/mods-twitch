from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Comando(models.Model):
    TIPO_COMANDO = (
        ('TODOS', 'Todos'),
        ('VIP', 'VIP'),
        ('MODERADOR', 'Moderador'),
        ('SUPERMOD', 'Supermod'),
    )
    ACTIVO = (
        (True, 'Activo'),
        (False, 'Inactivo'),
    )
    nombre_comando = models.CharField(max_length=20, unique=True)
    tipo_comando = models.CharField(max_length=10, choices=TIPO_COMANDO, default='TODOS')
    descripcion = models.CharField(max_length=100)
    activo = models.BooleanField(default=True, choices=ACTIVO)
    ejemplo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_comando
    
class Moderador(models.Model):
    MODERADOR = (
        ('ELCILANTROUWU', 'elcilantrouwu'),
        ('JOSHUAKOMODO', 'joshuakomodo'),
        ('KEDOP_19', 'kedop_19'),
        ('MELODYZOMBIE', 'MelodyZombie'),
        ('MRPONCHO345', 'mrponcho345'),
        ('POIYUTE', 'PoiYuTe'),
        ('CHACHOYVT', 'ChachoyVT'),
    )
    nombre_twitch = models.CharField(max_length=20, choices=MODERADOR, unique=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre_twitch
    
    def clean(self):
        # Verificar si este es un objeto existente (ya tiene ID)
        if self.pk:
            # Obtener el objeto original de la base de datos
            original = Moderador.objects.get(pk=self.pk)
            # Si el nombre de Twitch ha cambiado, lanzar error
            if original.nombre_twitch != self.nombre_twitch:
                raise ValidationError('El nombre de Twitch no puede ser modificado después de la creación.')
        super().clean()
    
class anuncios(models.Model):
    mensaje = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mensaje