from rest_framework.response import Response
from mascotas.models import Mascota
from mascotas.api_views.serializers import MascotaSerializer, PersonaSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import Http404


@api_view(['GET', 'POST'])
def mascotas_api_v1(request):
    if request.method == 'GET':
        mascotas = Mascota.objects.all()
        mascota_json = MascotaSerializer(mascotas, many=True)
        return Response(mascota_json.data)

    if request.method == 'POST':
        serializer = MascotaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_object(id):
    try:
        return Mascota.objects.get(id=id)
    except Mascota.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def mascotas_api_v1_pk(request, id):
    """
    Lista de mascota
    Crear mascota
    """
    if request.method == 'GET':
        mascota = get_object(id)
        serializer = MascotaSerializer(instance=mascota, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        mascota = get_object(id)
        serializer = MascotaSerializer(instance=mascota, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        mascota = get_object(id)
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def persona_mascota_api_v1(request, id_mascota):
    """
     Retorna el dueño de la mascota V1
    """
    try:
        mascota = Mascota.objects.get(id=id_mascota)
        persona = mascota.persona
    except Mascota.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        persona = PersonaSerializer(persona)
        return Response(persona.data, status=status.HTTP_200_OK)


