from rest_framework import serializers
from django.core.validators import EmailValidator
from .models import Comando, Moderador

class ComandoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comando
        fields = '__all__'
        extra_kwargs = {
            'descripcion': {'max_length': 1000},
            'comando': {'max_length': 100}
        }

class ModeradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moderador
        fields = '__all__'
        extra_kwargs = {
            'nombre_twitch': {'required': True},
            'alias': {'required': True},
            'email': {'required': True, 'validators': [EmailValidator()]},
            'password': {'write_only': True, 'required': True, 'style': {'input_type': 'password'}}
        }