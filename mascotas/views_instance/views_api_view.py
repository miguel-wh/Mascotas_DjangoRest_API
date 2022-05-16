import json
import requests
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from mascotas.forms import MascotaForm
from rest_framework import status

from mascotas.api_views.mascota_api_view import MascotaApiV2, MascotaApiV2PorPk


def lista_mascotas(request, api_version):
    mascotas_instance = MascotaApiV2.as_view()(request).data
    mascotas = mascotas_instance if 'id' in json.dumps(mascotas_instance) else {}
    return render(request, 'templates_apiview/lista_mascotas.html', {'mascotas': mascotas, 'api_version': api_version})


def crear_mascota(request, api_version):
    titulo = "Crear"
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():

            mascotas_instance = MascotaApiV2.as_view()(request).data
            return HttpResponseRedirect((reverse('lista_mascotas_views_apiview', args=[api_version])))
    else:
        form = MascotaForm()
    return render(request, 'templates_apiview/mascota_form.html', {
        'form': form, 'api_version': api_version, 'titulo': titulo,
    })


def editar_mascota(request, api_version, id):
    titulo = "Editar"
    form = MascotaForm(request.POST or None)

    if request.method == 'GET':
        mascotas_instance = MascotaApiV2PorPk.as_view()(request, id=id).data
        mascotas_data = mascotas_instance if 'id' in json.dumps(mascotas_instance) else {}

        mascotas_data['persona'] = mascotas_data.get('persona').get('id')
        mascotas_data['vacuna'] = [d['id'] for d in mascotas_data.get('vacuna')]

        form = MascotaForm(initial=mascotas_data)
    else:
        if form.is_valid():
            data = form.cleaned_data
            request.method = 'PUT'
            mascotas_instance = MascotaApiV2PorPk.as_view()(request, id=id).data
            return HttpResponseRedirect((reverse('lista_mascotas_views_apiview', args=[api_version])))

    return render(request, 'templates_apiview/mascota_form.html', {'form': form, 'api_version': api_version, 'titulo': titulo})


def eliminar_mascota(request, api_version, id):
    titulo = "Eliminar"
    if request.method == 'POST':

        request.method = 'DELETE'
        mascotas_instance = MascotaApiV2PorPk.as_view()(request, id=id).data
        return HttpResponseRedirect((reverse('lista_mascotas_views_apiview', args=[api_version])))

    else:
        request.method = 'GET'
        mascotas_instance = MascotaApiV2PorPk.as_view()(request, id=id).data
        mascota_data = mascotas_instance if 'id' in json.dumps(mascotas_instance) else {}
    return render(request, 'templates_apiview/eliminar_mascota.html',
                  {'mascota': mascota_data, 'api_version': api_version, "titulo": titulo})

