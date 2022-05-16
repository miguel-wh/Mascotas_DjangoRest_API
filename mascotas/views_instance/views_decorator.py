import json
import requests
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from mascotas.forms import MascotaForm
from rest_framework import status
from mascotas.api_views.mascota_decorador import mascotas_api_v1, mascotas_api_v1_pk, persona_mascota_api_v1


def lista_mascotas(request, api_version):
    mascotas_instance = mascotas_api_v1(request).data
    mascotas = mascotas_instance if 'id' in json.dumps(mascotas_instance) else {}
    return render(request, 'templates_decorador/lista_mascotas.html', {'mascotas': mascotas, 'api_version': api_version})


def crear_mascota(request, api_version):
    titulo = "Crear"
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():

            mascotas_instance = mascotas_api_v1(request).data
            return HttpResponseRedirect((reverse('lista_mascotas_views_decorador', args=[api_version])))
    else:
        form = MascotaForm()
    return render(request, 'templates_decorador/mascota_form.html', {
        'form': form, 'api_version': api_version, 'titulo': titulo,
    })


def editar_mascota(request, api_version, id):
    titulo = "Editar"
    form = MascotaForm(request.POST or None)

    if request.method == 'GET':
        mascotas_instance = mascotas_api_v1_pk(request, id=id).data
        mascotas_data = mascotas_instance if 'id' in json.dumps(mascotas_instance) else {}

        mascotas_data['persona'] = mascotas_data.get('persona').get('id')
        mascotas_data['vacuna'] = [d['id'] for d in mascotas_data.get('vacuna')]

        form = MascotaForm(initial=mascotas_data)
    else:
        if form.is_valid():
            data = form.cleaned_data
            request.method = 'PUT'
            mascotas_instance = mascotas_api_v1_pk(request, id=id).data
            return HttpResponseRedirect((reverse('lista_mascotas_views_decorador', args=[api_version])))

    return render(request, 'templates_decorador/mascota_form.html', {'form': form, 'api_version': api_version, 'titulo': titulo})


def eliminar_mascota(request, api_version, id):
    titulo = "Eliminar"
    if request.method == 'POST':

        request.method = 'DELETE'
        mascotas_instance = mascotas_api_v1_pk(request, id=id).data
        return HttpResponseRedirect((reverse('lista_mascotas', args=[api_version])))

    else:
        request.method = 'GET'
        mascotas_instance = mascotas_api_v1_pk(request, id=id).data
        mascota_data = mascotas_instance if 'id' in json.dumps(mascotas_instance) else {}
    return render(request, 'eliminar_mascota.html',
                  {'mascota': mascota_data, 'api_version': api_version, "titulo": titulo})


def ver_adoptante(request, api_version, id_mascota):
    adoptente = persona_mascota_api_v1(request, id_mascota).data
    adoptente_data = adoptente if 'id' in json.dumps(adoptente) else {}
    if type(adoptente_data) == list:
        adoptente_data = adoptente_data[0]

    return render(request, 'templates_decorador/ver_adoptante.html', {
        'api_version': api_version,
        'id_mascota': id_mascota,
        'adoptente_data': adoptente_data,
    })


