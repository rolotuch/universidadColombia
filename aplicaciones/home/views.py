from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.db.models.functions import Coalesce
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import PasswordChangeView,PasswordResetDoneView
from django.views.generic import RedirectView
from django.contrib.auth import logout

class IndexView(TemplateView):
    template_name = 'home/inicio.html'


class Home( TemplateView):
    template_name = 'home/home_page.html'
    login_url = 'home:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        context['entity'] = 'Home'
        context['list_url'] = "home:login"
        return context

class LogoutView(RedirectView):
    pattern_name = 'home:login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)

class MyPasswordChangeView(PasswordChangeView):
    template_name='home/change-password.html'
    success_url=reverse_lazy('home:pass_change_done')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cambiar Contraseña'
        context['entity'] = 'Cambiar Constraseña'
        context['list_url'] = "clinica/cambiar contrasñea"
        return context

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name='home/change-pass-done.html'