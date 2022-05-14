from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response

from mascotas.api_views.serializers import MascotaSerializer, PersonaSerializer

from mascotas.models import Mascota
from adopcion.models import Persona, Solicitud


class MascotaViewSet(viewsets.ViewSet):

    def list(self, request):

        queryset = Mascota.objects.all()
        serializer = MascotaSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):

        serializer = MascotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class MascotaViewSetPK(viewsets.ViewSet):

    def get_object(self, id):
        try:
            return Mascota.objects.get(id=id)
        except Mascota.DoesNotExist:
            raise Http404

    def retrieve(self, request, id):

        queryset = Mascota.objects.all()
        mascota = get_object_or_404(queryset, id=id)
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)

    def update(self, request, id):

        queryset = self.get_object(id)
        serializer = MascotaSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):

        queryset = self.get_object(id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PersonaMascotaApiV4(viewsets.ViewSet):
    """
     Retorna el dueño de la mascota V4
    """

    def get_object(self, pk):
        try:
            mascota = Mascota.objects.get(pk=pk)
            persona = mascota.persona
            return persona
        except Mascota.DoesNotExist:
            raise Http404

    def retrieve(self, request, pk=None):

        queryset = self.get_object(pk)
        serializer = PersonaSerializer(queryset)
        return Response(serializer.data)
