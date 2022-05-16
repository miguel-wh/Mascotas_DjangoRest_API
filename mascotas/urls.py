from django.urls import path

# Api V1
from mascotas.api_views.mascota_decorador import mascotas_api_v1, mascotas_api_v1_pk, persona_mascota_api_v1
# Api V2
from mascotas.api_views.mascota_api_view import MascotaApiV2, MascotaApiV2PorPk, PersonaMascotaApiV2
# Api V3
from mascotas.api_views.mascota_generic_view import MascotaGenericView, MascotaGenericViewPk, PersonaMascotaApiV3
# Api V4
from mascotas.api_views.mascota_viewset import MascotaViewSet, MascotaViewSetPK, PersonaMascotaApiV4

# Views
from mascotas.views import lista_mascotas, crear_mascota, editar_mascota, eliminar_mascota, ver_adoptante

from mascotas.views_instance import views_decorator, views_api_view, views_genericsviews, views_viewsets

urlpatterns = [

    # ###### ENDPOINTS #####

    # Con decorador @apiview - V1
    # Mascotas
    path('api/v1/', mascotas_api_v1, name="mascotas_api_v1"),  # GET, POST
    path('api/v1/<int:id>/', mascotas_api_v1_pk, name="mascotas_api_v1_pk"),  # DETAIL, PUT, DELETE
    # Persona-Mascota
    path('api/v1/<int:id_mascota>/persona/', persona_mascota_api_v1, name="persona_mascota_api_v1"),  # GET Persona

    # Con APIView - V2
    # Mascotas
    path('api/v2/', MascotaApiV2.as_view(), name="mascotas_api_v2"),  # GET, POST
    path('api/v2/<int:id>/', MascotaApiV2PorPk.as_view(), name="mascotas_api_v2_pk"),  # DETAIL, PUT, DELETE
    # Persona-Mascota
    path('api/v2/<int:id_mascota>/persona/', PersonaMascotaApiV2.as_view(), name="persona_mascota_api_v1"),  # GET Persona

    # Con GENERIC VIEW - V3
    # Mascotas
    path('api/v3/', MascotaGenericView.as_view(), name="mascotas_api_v3"),  # GET, POST
    path('api/v3/<int:pk>/', MascotaGenericViewPk.as_view(), name="mascotas_api_v3_pk"),  # DETAIL, PUT, DELETE
    # Persona-Mascota
    path('api/v3/<int:pk>/persona/', PersonaMascotaApiV3.as_view(), name="persona_mascota_api_v3"),  # GET Persona

    # Con ViewSets - V4
    path('api/v4/', MascotaViewSet.as_view({'get': 'list', 'post': 'create'}), name="mascotas_api_v4"),  # GET, POST
    path('api/v4/<int:id>/', MascotaViewSetPK.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'delete'}), name="mascotas_api_v4_pk"),  # DETAIL, PUT, DELETE
    # Persona-Mascota
    path('api/v4/<int:pk>/persona/', PersonaMascotaApiV4.as_view({'get': 'retrieve'}), name="persona_mascota_api_v4"),  # GET Persona


    # =========== VIEWS Para consumir endpoints con requests module ===========
    path('<str:api_version>/', lista_mascotas, name="lista_mascotas"),
    path('crear/<str:api_version>/', crear_mascota, name="crear_mascota"),
    path('editar/<str:api_version>/<int:id>', editar_mascota, name="editar_mascota"),
    path('eliminar/<str:api_version>/<int:id>', eliminar_mascota, name="eliminar_mascota"),

    path('<str:api_version>/adoptante/<int:id_mascota>/persona/', ver_adoptante, name="ver_adoptante"),

    # =========== VIEWS Para consumir endpoints con Instancias ===========
    # ####Decorador instance view

    path('views-decorador/<str:api_version>/', views_decorator.lista_mascotas, name="lista_mascotas_views_decorador"),
    path('views-decorador/crear/<str:api_version>/', views_decorator.crear_mascota, name="crear_mascotas_views_decorador"),
    path('views-decorador/editar/<str:api_version>/<int:id>/', views_decorator.editar_mascota, name="editar_mascotas_views_decorador"),
    path('views-decorador/eliminar/<str:api_version>/<int:id>', views_decorator.eliminar_mascota, name="eliminar_mascotas_views_decorador"),

    path('views-decorador/<str:api_version>/adoptante/<int:id_mascota>/persona/', views_decorator.ver_adoptante, name="ver_adoptante_views_decorador"),

    # ####APIVIews instance view

    path('views-apiview/<str:api_version>/', views_api_view.lista_mascotas, name="lista_mascotas_views_apiview"),
    path('views-apiview/crear/<str:api_version>/', views_api_view.crear_mascota, name="crear_mascotas_views_apiview"),
    path('views-apiview/editar/<str:api_version>/<int:id>/', views_api_view.editar_mascota, name="editar_mascotas_views_apiview"),
    path('views-apiview/eliminar/<str:api_version>/<int:id>', views_api_view.eliminar_mascota, name="eliminar_mascotas_views_apiview"),

    path('views-apiview/<str:api_version>/adoptante/<int:id_mascota>/persona/', views_api_view.ver_adoptante, name="ver_adoptante_views_apiview"),

    # ####Generics instance view

    path('views-generics/<str:api_version>/', views_genericsviews.lista_mascotas, name="lista_mascotas_views_genericsviews"),
    path('views-generics/crear/<str:api_version>/', views_genericsviews.crear_mascota, name="crear_mascotas_views_genericsviews"),
    path('views-generics/editar/<str:api_version>/<int:id>/', views_genericsviews.editar_mascota, name="editar_mascotas_views_genericsviews"),
    path('views-generics/eliminar/<str:api_version>/<int:id>', views_genericsviews.eliminar_mascota, name="eliminar_mascotas_views_genericsviews"),

    path('views-generics/<str:api_version>/adoptante/<int:id_mascota>/persona/', views_genericsviews.ver_adoptante, name="ver_adoptante_views_genericsviews"),

    # ####Generics instance view

    path('views-viewsets/<str:api_version>/', views_viewsets.lista_mascotas, name="lista_mascotas_views_viewsets"),
    path('views-viewsets/crear/<str:api_version>/', views_viewsets.crear_mascota, name="crear_mascotas_views_viewsets"),
    path('views-viewsets/editar/<str:api_version>/<int:id>/', views_viewsets.editar_mascota, name="editar_mascotas_views_viewsets"),
    path('views-viewsets/eliminar/<str:api_version>/<int:id>', views_viewsets.eliminar_mascota, name="eliminar_mascotas_views_viewsets"),

    path('views-viewsets/<str:api_version>/adoptante/<int:id_mascota>/persona/', views_viewsets.ver_adoptante, name="ver_adoptante_views_viewsets"),

]