import json
import requests
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from mascotas.forms import MascotaForm
from rest_framework import status
from mascotas.api_views.mascota_viewset import MascotaViewSet, MascotaViewSetPK


def lista_mascotas(request, api_version):
    mascotas_instance = MascotaViewSet.as_view({'get': 'list'})(request).data
    mascotas = mascotas_instance if 'id' in json.dumps(mascotas_instance) else {}
    return render(request, 'templates_viewsets/lista_mascotas.html', {'mascotas': mascotas, 'api_version': api_version})


def crear_mascota(request, api_version):
    titulo = "Crear"
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():

            mascotas_instance = MascotaViewSet.as_view({'post': 'create'})(request).data
            return HttpResponseRedirect((reverse('lista_mascotas_views_viewsets', args=[api_version])))
    else:
        form = MascotaForm()
    return render(request, 'templates_viewsets/mascota_form.html', {
        'form': form, 'api_version': api_version, 'titulo': titulo,
    })


def editar_mascota(request, api_version, id):
    titulo = "Editar"
    form = MascotaForm(request.POST or None)

    if request.method == 'GET':
        mascotas_instance = MascotaViewSetPK.as_view({'get': 'retrieve'})(request, id=id).data
        mascotas_data = mascotas_instance if 'id' in json.dumps(mascotas_instance) else {}

        mascotas_data['persona'] = mascotas_data.get('persona').get('id')
        mascotas_data['vacuna'] = [d['id'] for d in mascotas_data.get('vacuna')]

        form = MascotaForm(initial=mascotas_data)
    else:
        if form.is_valid():
            data = form.cleaned_data
            request.method = 'PUT'
            mascotas_instance = MascotaViewSetPK.as_view({'put': 'update'})(request, id=id).data
            return HttpResponseRedirect((reverse('lista_mascotas_views_viewsets', args=[api_version])))

    return render(request, 'templates_viewsets/mascota_form.html', {'form': form, 'api_version': api_version, 'titulo': titulo})


def eliminar_mascota(request, api_version, id):
    titulo = "Eliminar"
    if request.method == 'POST':

        request.method = 'DELETE'
        mascotas_instance = MascotaViewSetPK.as_view({'delete': 'delete'})(request, id=id).data
        return HttpResponseRedirect((reverse('lista_mascotas_views_viewsets', args=[api_version])))

    else:
        request.method = 'GET'
        mascotas_instance = MascotaViewSetPK.as_view({'get': 'retrieve'})(request, id=id).data
        mascota_data = mascotas_instance if 'id' in json.dumps(mascotas_instance) else {}
    return render(request, 'templates_viewsets/eliminar_mascota.html',
                  {'mascota': mascota_data, 'api_version': api_version, "titulo": titulo})

