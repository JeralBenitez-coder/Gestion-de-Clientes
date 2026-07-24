

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Cliente
from .serializers import ClienteSerializer, ClienteSerializerReg
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# LISTAR TODOS LOS CLIENTES (GET)

@api_view(['GET'])
def lista_clientes(request):
    clientes = Cliente.objects.all()
    serializer = ClienteSerializer(clientes, many=True)
    return Response(serializer.data)


# CREAR NUEVO CLIENTE (POST)

@swagger_auto_schema(
    method='post',
    operation_description='Añade un nuevo cliente.',
    request_body=ClienteSerializerReg,
    responses={201: 'Creado exitosamente', 400: 'Error en los datos'}
)
@api_view(['POST'])
def crear_clientes(request):
    serial_data = ClienteSerializerReg(data=request.data)
    if serial_data.is_valid():
        serial_data.save()
        return Response(serial_data.data, status=status.HTTP_201_CREATED)
    return Response(serial_data.errors, status=status.HTTP_400_BAD_REQUEST)


# VER UN SOLO CLIENTE (GET por ID)

@swagger_auto_schema(
    method='get',
    operation_description='Consulta los datos de un cliente por su ID.',
    responses={200: ClienteSerializerReg, 404: 'Cliente no encontrado'}
)
@api_view(['GET'])
def detalle_clientes(request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    serializer = ClienteSerializerReg(cliente)
    return Response(serializer.data)


# ACTUALIZAR CLIENTE (PUT)

@swagger_auto_schema(
    method='put',
    operation_description='Actualiza todos los datos de un cliente existente.',
    request_body=ClienteSerializerReg,
    responses={200: 'Actualizado', 400: 'Datos inválidos', 404: 'No encontrado'}
)
@api_view(['PUT'])
def actualizar_clientes(request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    serializer = ClienteSerializerReg(cliente, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'mensaje': 'Cliente actualizado exitosamente',
            'datos': serializer.data
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ELIMINAR CLIENTE (DELETE)

@swagger_auto_schema(
    method='delete',
    operation_description='Elimina un cliente de la base de datos.',
    responses={200: 'Eliminado', 404: 'Cliente no encontrado'}
)
@api_view(['DELETE'])
def eliminar_clientes(request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    cliente.delete()
    return Response({'mensaje': 'Cliente eliminado correctamente'}, status=status.HTTP_200_OK)