from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.db.models import Q

from core.users.models import User
from core.users.forms import UserForm, UpdateUserForm
from core.users.mixins import ValidatePermissionRequiredMixin
from core.utils.context_data import views


class UserListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = User
    template_name = 'user/list.html'
    permission_required = (
        'users.view_user',
        'users.add_user', 
        'users.change_user', 
        'users.delete_user',
    )
    paginate_by = 10

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[views.TITLE] = 'Usuarios'
        context[views.CREATE_URL] = reverse_lazy('users:user_create')
        context[views.LIST_URL] = reverse_lazy('users:user_list')
        context[views.ENTITY] = 'Usuarios'
        context[views.TITLE_ICON] = 'fas fa-search'
        context[views.HELP_SECTION] = 'list-user'

        # actions
        context[views.EDIT_BUTTON_URL] = reverse_lazy(
            'users:user_list') + "editar"
        context[views.DELETE_BUTTON_URL] = reverse_lazy(
            'users:user_list') + "asociados"

        return context
        

class UserCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = "user/create.html" 
    success_url = reverse_lazy('users:user_list')
    permission_required = (
        'users.view_user',
        'users.add_user', 
        'users.change_user', 
        'users.delete_user',
    )

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[views.TITLE] = 'Agregar nuevo usuario'
        context[views.LIST_URL] = reverse_lazy('users:user_list')
        context[views.ENTITY] = 'Usuarios'
        context[views.TITLE_ICON] = 'fas fa-plus'
        context[views.SAVE_BUTTON] = 'Guardar'
        return context
    
    
class UserUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "user/create.html" 
    success_url = reverse_lazy('users:user_list')
    permission_required = (
        'users.view_user',
        'users.add_user', 
        'users.change_user', 
        'users.delete_user',
    )

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[views.TITLE] = 'Editar usuario'
        context[views.LIST_URL] = reverse_lazy('users:user_list')
        context[views.ENTITY] = 'Usuarios'
        context[views.TITLE_ICON] = 'fas fa-edit'
        context[views.SAVE_BUTTON] = 'Guardar cambios'
        context[views.HELP_SECTION] = 'update-user'
        return context


class UserDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = User
    form_class = UserForm
    template_name = "user/delete.html" 
    success_url = reverse_lazy('users:user_list')
    permission_required = (
        'users.view_user',
        'users.add_user', 
        'users.change_user', 
        'users.delete_user',
    )

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[views.TITLE] = 'Eliminar usuario'
        context[views.LIST_URL] = reverse_lazy('users:user_list')
        context[views.ENTITY] = 'Usuarios'
        context[views.TITLE_ICON] = 'fas fa-trash'
        context[views.HELP_SECTION] = 'delete-user'
        return context