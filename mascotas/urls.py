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


    # =========== VIEWS Para consumir endpoints ===========
    path('<str:api_version>/', lista_mascotas, name="lista_mascotas"),
    path('crear/<str:api_version>/', crear_mascota, name="crear_mascota"),
    path('editar/<str:api_version>/<int:id>', editar_mascota, name="editar_mascota"),
    path('eliminar/<str:api_version>/<int:id>', eliminar_mascota, name="eliminar_mascota"),

    path('<str:api_version>/adoptante/<int:id_mascota>/persona/', ver_adoptante, name="ver_adoptante"),
]