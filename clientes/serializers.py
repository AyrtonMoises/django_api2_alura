from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self,data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"O CPF não é válido"})
        elif not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Informe somente letras no nome"})
        elif not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve conter 9 dígitos"})
        elif not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O Celular não está em formato válido 11 91234-1234"})
        return data