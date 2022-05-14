from django.http import Http404

# Django Rest Framework
from rest_framework import generics, status
from rest_framework.response import Response

# Models
from mascotas.models import Mascota
from adopcion.models import Persona, Solicitud

# Serializer
from mascotas.api_views.serializers import MascotaSerializer, PersonaSerializer


class MascotaGenericView(generics.ListCreateAPIView):
    """
    Lista de mascotas,
    Crear mascotas
    """
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer


class MascotaGenericViewPk(generics.RetrieveUpdateDestroyAPIView):
    """
    Ver mascota,
    Editar mascota,
    Eliminar mascota
    """
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer


class PersonaMascotaApiV3(generics.ListAPIView):
    """
     Retorna el dueño de la mascota V3
    """
    queryset = Persona.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            mascota = Mascota.objects.get(**kwargs)
        except Mascota.DoesNotExist:
            raise Http404
        queryset = self.get_queryset()
        queryset = queryset.filter(id=mascota.persona.id)
        serializer = PersonaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
