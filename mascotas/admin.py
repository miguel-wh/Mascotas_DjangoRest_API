from django.contrib import admin

from mascotas.models import Mascota, Vacuna

admin.site.register(Vacuna)
admin.site.register(Mascota)