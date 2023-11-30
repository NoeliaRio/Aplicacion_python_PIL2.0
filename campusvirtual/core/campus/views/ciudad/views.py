from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from core.users.mixins import ValidatePermissionRequiredMixin
from core.utils.context_data import views
from core.campus.models import Ciudad

class CiudadListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Ciudad
    template_name = 'ciudad/list.html'
    permission_required = (
        'users.view_ciudad',
        'users.add_ciudad', 
        'users.change_ciudad', 
        'users.delete_ciudad',
    )
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[views.TITLE] = 'Ciudades'
        #context[views.CREATE_URL] = reverse_lazy('users:area_create')
        context[views.LIST_URL] = reverse_lazy('campus:ciudad_list')
        context[views.ENTITY] = 'Ciudades'
        context[views.TITLE_ICON] = 'fas fa-search'

        # actions
        # context[views.EDIT_BUTTON_URL] = reverse_lazy(
        #     'users:area_list') + "editar"
        # context[views.DELETE_BUTTON_URL] = reverse_lazy(
        #     'users:area_list') + "asociados"

        return context

    def get_queryset(self):
        return Ciudad.objects.all()