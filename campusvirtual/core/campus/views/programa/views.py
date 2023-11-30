from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from core.users.mixins import ValidatePermissionRequiredMixin
from core.utils.context_data import views
from core.campus.models import Programa

class ProgramaListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Programa
    template_name = 'programa/list.html'
    permission_required = (
        'users.view_programa',
        'users.add_programa', 
        'users.change_programa', 
        'users.delete_programa',
    )
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[views.TITLE] = 'Programa'
        #context[views.CREATE_URL] = reverse_lazy('users:area_create')
        context[views.LIST_URL] = reverse_lazy('campus:programa_list')
        context[views.ENTITY] = 'Programa'
        context[views.TITLE_ICON] = 'fas fa-search'

        # actions
        # context[views.EDIT_BUTTON_URL] = reverse_lazy(
        #     'users:area_list') + "editar"
        # context[views.DELETE_BUTTON_URL] = reverse_lazy(
        #     'users:area_list') + "asociados"

        return context

    def get_queryset(self):
        return Programa.objects.all()