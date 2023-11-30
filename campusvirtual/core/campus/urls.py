from django.urls import path
from core.users.views.user.views import *

from core.campus.views.pais.views import *
from core.campus.views.provincia.views import *
from core.campus.views.ciudad.views import *
from core.campus.views.barrio.views import *
from core.campus.views.universidad.views import *
from core.campus.views.facultad.views import *
from core.campus.views.campus.views import *
from core.campus.views.programa.views import *

app_name = 'campus'
urlpatterns = [
    # Datos universitarios
    path('universidades/', UniversidadListView.as_view(), name='universidad_list'),
    path('facultades/', FacultadListView.as_view(), name='facultad_list'),
    path('campus/', CampusListView.as_view(), name='campus_list'),
    path('programas/', ProgramaListView.as_view(), name='programa_list'),

    # Lugares
    path('paises/', PaisListView.as_view(), name='pais_list'),
    path('provincias/', ProvinciaListView.as_view(), name='provincia_list'),
    path('ciudades/', CiudadListView.as_view(), name='ciudad_list'),
    path('barrios/', BarrioListView.as_view(), name='barrio_list'),
]