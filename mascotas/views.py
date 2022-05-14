import requests
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from mascotas.forms import MascotaForm
from rest_framework import status


def lista_mascotas(request, api_version):

    mascotas = requests.get(f'http://127.0.0.1:8000/mascotas/api/{api_version}/')
    mascotas = mascotas.json()

    return render(request, 'lista_mascotas.html', {'mascotas': mascotas, 'api_version': api_version})


def crear_mascota(request, api_version):
    titulo = "Crear"
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():

            payload = {
                'nombre': form.data.get('nombre'),
                'sexo': form.data.get('sexo'),
                'edad_aproximada': form.data.get('edad_aproximada'),
                'fecha_rescate': form.data.get('fecha_rescate'),
                'persona':  form.data.get('persona'),
                'vacuna': [form.data.get('vacuna')],

            }

            mascota_response = requests.post(f'http://127.0.0.1:8000/mascotas/api/{api_version}/', json=payload)

            if mascota_response.status_code == 201:  # Creado
                return HttpResponseRedirect((reverse('lista_mascotas', args=[api_version])))

    else:
        form = MascotaForm()
    return render(request, 'mascota_form.html', {
        'form': form, 'api_version': api_version, 'titulo': titulo,
    })


def editar_mascota(request, api_version, id):
    titulo = "Editar"
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            pass
            payload = {
                'nombre': form.data.get('nombre'),
                'sexo': form.data.get('sexo'),
                'edad_aproximada': form.data.get('edad_aproximada'),
                'fecha_rescate': form.data.get('fecha_rescate'),
                'persona': form.data.get('persona'),
                'vacuna': [form.data.get('vacuna')],

            }
            requests.put(f'http://127.0.0.1:8000/mascotas/api/{api_version}/{id}/', json=payload)
            return HttpResponseRedirect((reverse('lista_mascotas', args=[api_version])))
    else:

        mascotas = requests.get(f'http://127.0.0.1:8000/mascotas/api/{api_version}/{id}/')
        mascotas_data = mascotas.json()
        mascotas_data['persona'] = mascotas_data.get('persona').get('id')
        mascotas_data['vacuna'] = [d['id'] for d in mascotas_data.get('vacuna')]

        form = MascotaForm(initial=mascotas_data)

    return render(request, 'mascota_form.html', {'form': form, 'api_version': api_version, 'titulo': titulo})


def eliminar_mascota(request, api_version, id):
    titulo = "Eliminar"
    if request.method == 'POST':

        mascota = requests.delete(f'http://127.0.0.1:8000/mascotas/api/{api_version}/{id}/')
        if mascota.status_code == status.HTTP_204_NO_CONTENT:
            return HttpResponseRedirect((reverse('lista_mascotas', args=[api_version])))

    else:
        mascota = requests.get(f'http://127.0.0.1:8000/mascotas/api/{api_version}/{id}/')
        mascota_data = mascota.json()
    return render(request, 'eliminar_mascota.html', {'mascota': mascota_data, 'api_version': api_version, "titulo": titulo})


def ver_adoptante(request, api_version, id_mascota):
    adoptente = requests.get(f'http://127.0.0.1:8000/mascotas/api/{api_version}/{id_mascota}/persona/')
    adoptente_data = adoptente.json()
    if type(adoptente_data) == list:
        adoptente_data = adoptente_data[0]

    return render(request, 'ver_adoptante.html', {
        'api_version': api_version,
        'id_mascota': id_mascota,
        'adoptente_data': adoptente_data,
    })


