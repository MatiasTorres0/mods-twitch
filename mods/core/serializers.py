from dataclasses import fields
from traceback import extract_stack
from rest_framework import serializers
from django.core.validators import EmailValidator
from .models import Comando, Moderador, Combate_WWE, Notas_Mods


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

class NotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notas_Mods
        fields = '__all__'
        extra_kwargs = {
            'Titulo': {'required': True},
            'contenido': {'required': True},
            'categoria': {'required': True},
            'prioridad': {'required': True},
            'fecha': {
                'required': True,
                'style': {'input_type': 'date'},
                'format': '%d-%m-%Y',
                'validators': [
                    serializers.DateField(
                        format='%d-%m-%Y',
                        input_formats=['%d-%m-%Y'],
                        error_messages={
                            'invalid': 'Date must be in DD-MM-YYYY format'
                        }
                    )
                ]
            }
        }

class Combate_WWESerializer(serializers.ModelSerializer):
    # Validate that luchador fields are different from each other
    def validate(self, data):
        luchadores = [
            data.get('luchador_1'),
            data.get('luchador_2'),
            data.get('luchador_3'),
            data.get('luchador_4')
        ]
        if len(set(luchadores)) != len(luchadores):
            raise serializers.ValidationError("All wrestlers must be different")
        return data

    class Meta:
        model = Combate_WWE
        fields = '__all__'
        extra_kwargs = {
            'stream': {'required': True},
            'tipo_combate': {'required': True},
            'luchador_1': {'required': True},
            'luchador_2': {'required': True},
            'luchador_3': {'required': True},
            'luchador_4': {'required': True},
            'resultado': {'required': True},
            'orden_combate': {'required': True}
        }