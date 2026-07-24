from rest_framework import serializers
from .models import Cliente


# Serializador para listar y ver detalles
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'  # Trae todos los campos, incluido el id automático


# Serializador para crear y actualizar clientes
class ClienteSerializerReg(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'edad', 'email']