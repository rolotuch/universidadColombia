from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View, FormView
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.messages.views import SuccessMessageMixin

from aplicaciones.config.views import SinPrivilegios, ValidatePermissionRequiredMixin
from .models import Usuario
from .forms import UserForm, UserProfileForm

class UserListView(SuccessMessageMixin, SinPrivilegios, ListView):
    permission_required = 'view_usuario'
    model = Usuario
    template_name = "usuarios/listar.html"
    context_object_name = "obj"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Datos del usuario'
        context['create_url'] = reverse_lazy('admon:user_new')
        context['list_url'] = reverse_lazy('admon:user_list')
        context['entity'] = 'Usuario'
        return context


class UserCreateView(SinPrivilegios, SuccessMessageMixin, CreateView):
    permission_required = 'add_usuario'
    model = Usuario
    form_class = UserForm
    template_name = 'usuarios/add.html'
    success_url = reverse_lazy('admon:user_list')
    context_object_name = "obj"
    success_message = "Registro "" '%(username)s '"" Creado Satisfactoriamente"
    error_message = "Error al Intentar crear el Usuario, verifique los datos"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)

    def form_submit(self, request):
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                messages.error(request, self.error_message)

            return HttpResponseRedirect(self.success_url)
        return self.success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Usuario'
        context['entity'] = 'Usuarios'
        context['list_url'] = self.success_url

        return context


class UserEditView(SinPrivilegios, SuccessMessageMixin, UpdateView):
    permission_required = 'change_usuario'
    model = Usuario
    form_class = UserForm
    template_name = 'usuarios/add.html'
    success_url = reverse_lazy('admon:user_list')
    context_object_name = "obj"
    success_message = "Registro "" ' %(username)s ' "" Actualizado Satisfactoriamente"
    error_message = "Error al actualizar el registro "" '%(username)s' "", verifique los Campos."

    def form_valid(self, form):
        form.instance.modified_by = self.request.user
        return super().form_valid(form)

    def form_submit(self, request):
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                messages.success(self.request, self.success_message)
                form.save()
            else:
                messages.error(self.request, self.error_message)
            return HttpResponseRedirect(self.success_url)
        return self.success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Datos'
        context['entity'] = 'Usuario'
        context['list_url'] = self.success_url
        return context


class UsuarioDeleteView(SinPrivilegios, SuccessMessageMixin, DeleteView):
    permission_required = "delete_usuario"
    model = Usuario
    template_name = 'usuarios/del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy("admon:user_list")
    success_message = "Registro "" '%(username)s' "" Eliminado Satisfactoriamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Usuario'
        context['entity'] = 'Usuario'
        context['list_url'] = self.success_url
        return context


class UserDetalleView(SuccessMessageMixin, DetailView):
    model = Usuario
    template_name = 'usuarios/detalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle de '
        context['entity'] = 'Usuario'
        context['volver'] = reverse_lazy('admon:user_list')
        context['encabezado'] = 'Detalle de usuario'
        # context['list_url'] = self.success_url
        return context


class UserChangeGroup(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            request.session['group'] = Group.objects.get(pk=self.kwargs['pk'])
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('bases:home'))


class UserPerfilView(SinPrivilegios, SuccessMessageMixin, UpdateView):
    model = Usuario
    form_class = UserProfileForm
    template_name = 'usuarios/perfil.html'
    success_url = reverse_lazy('admon:user_list')
    context_object_name = "obj"
    permission_required = 'change_usuario'
    success_message = "Registro "" '%(username)s' "" Actualizado Satisfactoriamente"
    error_meesage = "Error al actualizar el registro "" '%(username)s' "" verifique los Campos ."

    url_redirect = success_url

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.instance.u_m = self.request.user
        return super().form_valid(form)

    def form_submit(self, request):
        if request.method == 'POST':
            form = UserProfileForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                messages.error(self.request, self.error_message)
            return HttpResponseRedirect(self.url_redirect)
        return self.url_redirect

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Perfil'
        context['entity'] = '/Usuario/Perfil'
        context['list_url'] = self.success_url
        return context


class PasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, FormView):
    model = Usuario
    form_class = PasswordChangeForm
    success_url = reverse_lazy('bases:login')
    template_name = 'usuarios/change_pass.html'
    success_message = 'Datos Actualizados Satisfactoriamente'
    error_message = 'error'

    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super(PasswordChangeView, self).form_invalid(form)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Datos almacenados satisfactoriamente')
        update_session_auth_hash(self.request, form.user)
        return super(PasswordChangeView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Password'
        context['entity'] = 'Password'
        context['list_url'] = self.success_url
        return context
