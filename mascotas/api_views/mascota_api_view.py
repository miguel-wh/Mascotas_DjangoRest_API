from mascotas.models import Mascota
from mascotas.api_views.serializers import MascotaSerializer, PersonaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class MascotaApiV2(APIView):
    """
    Lista de mascota
    Crear mascota
    """
    def get(self, request):
        mascotas = Mascota.objects.all()
        mascotas_serializer = MascotaSerializer(mascotas, many=True)
        return Response(mascotas_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        mascotas_serializer = MascotaSerializer(data=request.data)
        if mascotas_serializer.is_valid():
            mascotas_serializer.save()
            return Response(mascotas_serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(mascotas_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MascotaApiV2PorPk(APIView):
    """
    Detalles Mascota
    Editar Mascota
    Borrar Mascota
    """
    def get_object(self, id):
        try:
            return Mascota.objects.get(id=id)
        except Mascota.DoesNotExist:
            raise Http404

    def get(self, request, id):
        mascota = self.get_object(id)
        serializer_mascota = MascotaSerializer(instance=mascota, many=False)
        return Response(serializer_mascota.data)

    def put(self, request, id):
        mascota = self.get_object(id)
        serializer_mascota = MascotaSerializer(mascota, data=request.data)
        if serializer_mascota.is_valid():
            serializer_mascota.save()
            return Response(serializer_mascota.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer_mascota.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        mascotas = self.get_object(id)
        mascotas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PersonaMascotaApiV2(APIView):
    """
     Retorna el dueño de la mascota V2
    """
    def get_object(self, id_mascota):

        try:
            mascota = Mascota.objects.get(id=id_mascota)
            persona = mascota.persona
            return persona
        except Mascota.DoesNotExist:
            raise Http404

    def get(self, request, id_mascota):
        persona = self.get_object(id_mascota)
        serializer_persona = PersonaSerializer(persona)
        return Response(serializer_persona.data, status=status.HTTP_200_OK)
