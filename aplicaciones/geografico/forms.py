from django import forms
from django.forms import ModelForm
from .models import Pais, Departamento, Ciudad, Conocimiento, Formacion


class PaisForm(ModelForm):
    """PaisForm definition."""

    # TODO: Define form fields here
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })                        
            self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Pais
        fields = ['nombre', 'state']

        widgets = {
            'nombre': forms.TextInput(
                attrs={'placeholder': 'Pais', 'class': 'input-group-field', 'help_text': '.', }),
            'state': forms.widgets.CheckboxInput(attrs={'class': 'form-check icheck-primary d-inline', }),
        }
        exclude = ['created_date', 'modified_date', 'deleted_date', 'created_by', 'modified_by']


    def clean(self):
        try:
            sc = Pais.objects.get(
                nombre=self.cleaned_data["nombre"]
            )

            if not self.instance.pk:
                raise forms.ValidationError("Registro Ya Existe")
            elif self.instance.pk != sc.pk:
                raise forms.ValidationError("Cambio No Permitido")
        except Pais.DoesNotExist:
            pass
        return self.cleaned_data

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():

                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class DepartamentoForm(ModelForm):
    """PaisForm definition."""

    # TODO: Define form fields here
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Departamento
        fields = ['pais', 'nombre', 'state']

        widgets = {
            'nombre': forms.TextInput(
                attrs={'placeholder': 'Departamento', 'class': 'input-group-field', 'help_text': '.', }),
            'state': forms.widgets.CheckboxInput(attrs={'class': 'form-check icheck-primary d-inline', }),

        }
        exclude = ['created_date', 'modified_date',
                   'deleted_date', 'created_by', 'modified_by']

    def clean(self):
        try:
            sc = Departamento.objects.get(
                nombre=self.cleaned_data["nombre"]
            )

            if not self.instance.pk:
                raise forms.ValidationError("Registro Ya Existe")
            elif self.instance.pk != sc.pk:
                raise forms.ValidationError("Cambio No Permitido")
        except Departamento.DoesNotExist:
            pass
        return self.cleaned_data

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():

                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class CiudadForm(ModelForm):
    """PaisForm definition."""

    # TODO: Define form fields here
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Ciudad
        fields = ['departamento', 'nombre', 'state']

        widgets = {
            'nombre': forms.TextInput(
                attrs={'placeholder': 'Ciudad', 'class': 'input-group-field', 'help_text': '.', }),
            'state': forms.widgets.CheckboxInput(attrs={'class': 'form-check icheck-primary d-inline', }),

        }
        exclude = ['created_date', 'modified_date',
                   'deleted_date', 'created_by', 'modified_by']

    def clean(self):
        try:
            sc = Ciudad.objects.get(
                nombre=self.cleaned_data["nombre"]
            )

            if not self.instance.pk:
                raise forms.ValidationError("Registro Ya Existe")
            elif self.instance.pk != sc.pk:
                raise forms.ValidationError("Cambio No Permitido")
        except Ciudad.DoesNotExist:
            pass
        return self.cleaned_data

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():

                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class ConocimientoForm(ModelForm):
    """PaisForm definition."""

    # TODO: Define form fields here
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descripcion'].widget.attrs['autofocus'] = True

    class Meta:
        model = Conocimiento
        fields = ['descripcion', 'state']

        widgets = {
            'descripcion': forms.TextInput(
                attrs={'placeholder': 'Conocimiento', 'class': 'input-group-field', 'help_text': '.', }),
            'state': forms.widgets.CheckboxInput(attrs={'class': 'form-check icheck-primary d-inline', }),

        }
        exclude = ['created_date', 'modified_date',
                   'deleted_date', 'created_by', 'modified_by']

    def clean(self):
        try:
            sc = Conocimiento.objects.get(
                descripcion=self.cleaned_data["descripcion"]
            )

            if not self.instance.pk:
                raise forms.ValidationError("Registro Ya Existe")
            elif self.instance.pk != sc.pk:
                raise forms.ValidationError("Cambio No Permitido")
        except Conocimiento.DoesNotExist:
            pass
        return self.cleaned_data

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():

                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
class FormacionForm(ModelForm):
    """PaisForm definition."""

    # TODO: Define form fields here
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Formacion
        fields = ['nombre', 'descripcion', 'state']

        widgets = {
            'nombre': forms.TextInput(
                attrs={'placeholder': 'Ciudad', 'class': 'input-group-field', 'help_text': '.', }),
            'descripcion': forms.TextInput(
                attrs={'placeholder': 'Ciudad', 'class': 'input-group-field', 'help_text': '.', }),
            'state': forms.widgets.CheckboxInput(attrs={'class': 'form-check icheck-primary d-inline', }),

        }
        exclude = ['created_date', 'modified_date',
                   'deleted_date', 'created_by', 'modified_by']

    def clean(self):
        try:
            sc = Formacion.objects.get(
                nombre=self.cleaned_data["nombre"]
            )

            if not self.instance.pk:
                raise forms.ValidationError("Registro Ya Existe")
            elif self.instance.pk != sc.pk:
                raise forms.ValidationError("Cambio No Permitido")
        except Formacion.DoesNotExist:
            pass
        return self.cleaned_data

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():

                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

