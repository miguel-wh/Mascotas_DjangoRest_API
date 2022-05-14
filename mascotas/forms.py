from django import forms

from mascotas.models import Vacuna
from adopcion.models import Persona


class MascotaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=False)
    sexo = forms.CharField(max_length=30, required=False)
    edad_aproximada = forms.IntegerField(required=False)
    fecha_rescate = forms.DateField(required=False)
    persona = forms.ModelChoiceField(required=False, queryset=Persona.objects.all())
    vacuna = forms.ModelChoiceField(required=False, queryset=Vacuna.objects.all())

    # class Meta:
    #
    #
    #     fields = [
    #         'nombre',
    #         'sexo',
    #         'edad_aproximada',
    #         'fecha_rescate',
    #         'persona',
    #         'image',
    #         'vacuna',
    #
    #     ]
    #     labels = {
    #         'nombre': 'Nombre de  la Mascota',
    #         'sexo': 'Sexo',
    #         'edad_aproximada': 'Edad aproximada',
    #         'fecha_rescate':'Fecha de rescate',
    #         'persona': 'Adoptante',
    #         'image': 'Imagen:',
    #         'vacuna': 'Vacunas',
    #     }
    #     widgets = {
    #         'nombre': forms.TextInput(attrs={'class':'form-control'}),
    #         'sexo': forms.TextInput(attrs={'class':'form-control'}),
    #         'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
    #         'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
    #         'persona': forms.Select(attrs={'class':'form-control'}),
    #         'vacuna': forms.CheckboxSelectMultiple(),
    #     }
