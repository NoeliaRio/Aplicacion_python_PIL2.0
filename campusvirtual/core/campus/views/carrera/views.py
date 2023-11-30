from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from core.users.mixins import ValidatePermissionRequiredMixin
from core.utils.context_data import views
from core.campus.models import Carrera

class CarreraListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Carrera
    template_name = 'carrera/list.html'
    permission_required = (
        'users.view_carrera',
        'users.add_carrera', 
        'users.change_carrera', 
        'users.delete_carrera',
    )
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[views.TITLE] = 'Carrera'
        #context[views.CREATE_URL] = reverse_lazy('users:area_create')
        context[views.LIST_URL] = reverse_lazy('campus:carrera_list')
        context[views.ENTITY] = 'Carrera'
        context[views.TITLE_ICON] = 'fas fa-search'

        # actions
        # context[views.EDIT_BUTTON_URL] = reverse_lazy(
        #     'users:area_list') + "editar"
        # context[views.DELETE_BUTTON_URL] = reverse_lazy(
        #     'users:area_list') + "asociados"

        return context

    def get_queryset(self):
        return Carrera.objects.all()