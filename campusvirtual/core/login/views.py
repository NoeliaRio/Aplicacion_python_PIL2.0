from django.contrib.auth.views import AuthenticationForm
from django.views.generic import FormView, RedirectView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import config.settings.base as setting


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy(setting.LOGIN_REDIRECT_URL)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
           return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context


class LoginRedirectView(RedirectView):
    pattern_name = 'login:login_form'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
