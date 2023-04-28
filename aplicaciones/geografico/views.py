
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect, JsonResponse

from django.contrib.auth.decorators import login_required, permission_required

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from aplicaciones.config.views import SinPrivilegios, ValidatePermissionRequiredMixin


from .models import Pais, Departamento, Ciudad, Conocimiento, Formacion
from .forms import  PaisForm, DepartamentoForm, CiudadForm, ConocimientoForm, FormacionForm

class PaisListView(SinPrivilegios, ValidatePermissionRequiredMixin, SuccessMessageMixin, ListView):
    permission_required = 'geografico.view_pais'
    model = Pais
    template_name = "pais/read.html"
    error_message = "Error al actualizar el registro, verifique los Campos."
    context_object_name = "obj"   
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Datos del Pais'
        context['create_url'] = reverse_lazy('geografico:pais_new')
        context['list_url'] = reverse_lazy('geografico:pais_list')
        context['entity'] = 'Pais'
        #context['edad'] = Paciente.objects.get_edad()
        return context


class PaisNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "add_pais"
    model = Pais
    template_name = "pais/add.html"
    context_object_name = "obj"
    form_class = PaisForm
    success_url = reverse_lazy("geografico:pais_list")
   
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de pais'
        context['entity'] = 'Pais_Crear'
        context['list_url'] = reverse_lazy("geografico:pais_list")
        context['action'] = 'add'
        return context


class PaisEdit(SuccessMessageMixin, SinPrivilegios, ValidatePermissionRequiredMixin, UpdateView):
    permission_required = "change_pais"
    model = Pais
    template_name = "pais/add.html"
    context_object_name = "obj"
    form_class = PaisForm
    success_url = reverse_lazy("geografico:pais_list")
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Datos'
        context['entity'] = 'Pais'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        #context['edad'] = self.get_edad()
        
        return context


@login_required(login_url='/login/')
@permission_required('geografico.change_pais', login_url='/login/')
def pais_inactivar(request, id):
    pais = Pais.objects.filter(pk=id).first()

    if request.method=='POST':
        if pais:
            pais.state= not pais.state
            pais.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")    
    return HttpResponse("FAIL")
    

class DepartamentoListView(SinPrivilegios, ValidatePermissionRequiredMixin, SuccessMessageMixin, ListView):
    permission_required = 'geografico.view_departamento'
    model = Departamento
    template_name = "departamento/read.html"
    error_message = "Error al actualizar el registro, verifique los Campos."
    context_object_name = "obj"   
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Datos del departamento'
        context['create_url'] = reverse_lazy('geografico:depto_new')
        context['list_url'] = reverse_lazy('geografico:depto_list')
        context['entity'] = 'Departamento'
        
        return context


class DepartamentoNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "add_departamento"
    model = Departamento
    template_name = "departamento/add.html"
    context_object_name = "obj"
    form_class = DepartamentoForm
    success_url = reverse_lazy("geografico:depto_list")
   
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de departamento'
        context['entity'] = 'Departamento_Crear'
        context['list_url'] = reverse_lazy("geografico:depto_list")
        context['action'] = 'add'
        return context


class DepartamentoEdit(SuccessMessageMixin, SinPrivilegios, ValidatePermissionRequiredMixin, UpdateView):
    permission_required = "change_departamento"
    model = Departamento
    template_name = "departamento/add.html"
    context_object_name = "obj"
    form_class = DepartamentoForm
    success_url = reverse_lazy("geografico:depto_list")
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Datos'
        context['entity'] = 'Departamento'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        #context['edad'] = self.get_edad()
        
        return context


@login_required(login_url='/login/')
@permission_required('geografico.change_departamento', login_url='/login/')
def depto_inactivar(request, id):
    departamento = Departamento.objects.filter(pk=id).first()

    if request.method=='POST':
        if departamento:
            departamento.state= not departamento.state
            departamento.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")    
    return HttpResponse("FAIL")


class CiudadListView(SinPrivilegios, ValidatePermissionRequiredMixin, SuccessMessageMixin, ListView):
    permission_required = 'geografico.view_ciudad'
    model = Ciudad
    template_name = "ciudad/read.html"
    error_message = "Error al actualizar el registro, verifique los Campos."
    context_object_name = "obj"   
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Datos del departamento'
        context['create_url'] = reverse_lazy('geografico:ciudad_new')
        context['list_url'] = reverse_lazy('geografico:ciudad_list')
        context['entity'] = 'Ciudad'
        
        return context


class CiudadNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "add_ciudad"
    model = Ciudad
    template_name = "ciudad/add.html"
    context_object_name = "obj"
    form_class = CiudadForm
    success_url = reverse_lazy("geografico:ciudad_list")
   
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Ciudad'
        context['entity'] = 'Ciudad_Crear'
        context['list_url'] = reverse_lazy("geografico:ciudad_list")
        context['action'] = 'add'
        return context


class CiudadEdit(SuccessMessageMixin, SinPrivilegios, ValidatePermissionRequiredMixin, UpdateView):
    permission_required = "change_ciudad"
    model = Ciudad
    template_name = "departamento/add.html"
    context_object_name = "obj"
    form_class = CiudadForm
    success_url = reverse_lazy("geografico:ciudad_list")
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Datos'
        context['entity'] = 'Ciudad'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        #context['edad'] = self.get_edad()
        
        return context


@login_required(login_url='/login/')
@permission_required('geografico.change_ciudad', login_url='/login/')
def ciudad_inactivar(request, id):
    ciudad = Ciudad.objects.filter(pk=id).first()

    if request.method=='POST':
        if ciudad:
            ciudad.state= not ciudad.state
            ciudad.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")    
    return HttpResponse("FAIL")

class ConocimientoListView(SinPrivilegios, ValidatePermissionRequiredMixin, SuccessMessageMixin, ListView):
    permission_required = 'geografico.view_conocimiento'
    model = Conocimiento
    template_name = "conocimiento/read.html"
    error_message = "Error al actualizar el registro, verifique los Campos."
    context_object_name = "obj"   
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Datos del conocimiento'
        context['create_url'] = reverse_lazy('geografico:cono_new')
        context['list_url'] = reverse_lazy('geografico:cono_list')
        context['entity'] = 'Conocimiento'
        
        return context


class ConocimientoNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "add_conocimiento"
    model = Conocimiento
    template_name = "ciudad/add.html"
    context_object_name = "obj"
    form_class = ConocimientoForm
    success_url = reverse_lazy("geografico:cono_list")
   
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de conocimiento'
        context['entity'] = 'Conocimiento_Crear'
        context['list_url'] = reverse_lazy("geografico:cono_list")
        context['action'] = 'add'
        return context


class ConocimientoEdit(SuccessMessageMixin, SinPrivilegios, ValidatePermissionRequiredMixin, UpdateView):
    permission_required = "change_conocimiento"
    model = Ciudad
    template_name = "conocimiento/add.html"
    context_object_name = "obj"
    form_class = CiudadForm
    success_url = reverse_lazy("geografico:cono_list")
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Datos'
        context['entity'] = 'Conocimiento'
        context['list_url'] = self.success_url
        context['action'] = 'edit'                
        return context


@login_required(login_url='/login/')
@permission_required('geografico.change_conocimiento', login_url='/login/')
def cono_inactivar(request, id):
    cono = Conocimiento.objects.filter(pk=id).first()

    if request.method=='POST':
        if cono:
            cono.state= not cono.state
            cono.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")    
    return HttpResponse("FAIL")

class FormacionListView(SinPrivilegios, ValidatePermissionRequiredMixin, SuccessMessageMixin, ListView):
    permission_required = 'geografico.view_formacion'
    model = Formacion
    template_name = "formacion/read.html"
    error_message = "Error al actualizar el registro, verifique los Campos."
    context_object_name = "obj"   
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Datos del Formacion'
        context['create_url'] = reverse_lazy('geografico:form_new')
        context['list_url'] = reverse_lazy('geografico:form_list')
        context['entity'] = 'Formacion'
        
        return context


class FormacionNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "add_formacion"
    model = Formacion
    template_name = "formacion/add.html"
    context_object_name = "obj"
    form_class = FormacionForm
    success_url = reverse_lazy("geografico:form_list")
   
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de formacion'
        context['entity'] = 'Formacion_Crear'
        context['list_url'] = reverse_lazy("geografico:form_list")
        context['action'] = 'add'
        return context


class FormacionEdit(SuccessMessageMixin, SinPrivilegios, ValidatePermissionRequiredMixin, UpdateView):
    permission_required = "change_formacion"
    model = Formacion
    template_name = "formacion/add.html"
    context_object_name = "obj"
    form_class = FormacionForm
    success_url = reverse_lazy("geografico:form_list")
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Datos'
        context['entity'] = 'Formacion'
        context['list_url'] = self.success_url
        context['action'] = 'edit'                
        return context


@login_required(login_url='/login/')
@permission_required('geografico.change_formacion', login_url='/login/')
def form_inactivar(request, id):
    form = Formacion.objects.filter(pk=id).first()

    if request.method=='POST':
        if form:
            form.state= not form.state
            form.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")    
    return HttpResponse("FAIL")
