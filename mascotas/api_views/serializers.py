from rest_framework import serializers
from mascotas.models import Mascota, Vacuna
from adopcion.models import Persona


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'


class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = '__all__'


class MascotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mascota
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['vacuna'] = VacunaSerializer(read_only=True, many=True)
        self.fields['persona'] = PersonaSerializer(read_only=True)
        return super(MascotaSerializer, self).to_representation(instance)


