from django.urls import path
from core.users.views.user.views import *

from core.users.views.genero.views import GeneroListView
from core.users.views.tipouser.views import TipoUserListView

app_name = 'users'
urlpatterns = [
    # Géneros
    path('generos/', GeneroListView.as_view(), name='genero_list'),

    # Tipos de usuario
    path('tipousuarios/', TipoUserListView.as_view(), name='tipouser_list'),

    path('', UserListView.as_view(), name='user_list'),
    path('agregar/', UserCreateView.as_view(), name='user_create'),
    path('editar/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('eliminar/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]