from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from core.users.mixins import ValidatePermissionRequiredMixin
from core.utils.context_data import views
from core.users.models import Genero

class GeneroListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Genero
    template_name = 'genero/list.html'
    permission_required = (
        'users.view_genero',
        'users.add_genero', 
        'users.change_genero', 
        'users.delete_genero',
    )
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[views.TITLE] = 'Géneros'
        #context[views.CREATE_URL] = reverse_lazy('users:area_create')
        context[views.LIST_URL] = reverse_lazy('users:genero_list')
        context[views.ENTITY] = 'Géneros'
        context[views.TITLE_ICON] = 'fas fa-search'

        # actions
        # context[views.EDIT_BUTTON_URL] = reverse_lazy(
        #     'users:area_list') + "editar"
        # context[views.DELETE_BUTTON_URL] = reverse_lazy(
        #     'users:area_list') + "asociados"

        return context

    def get_queryset(self):
        return Genero.objects.all()