from django import forms
from django.forms import ModelForm
from .models import Usuario


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autofocus'] = True

    class Meta:
        model = Usuario
        fields = ['avatar', 'username', 'password', 'first_name', 'last_name', 'telefono', 'genero', 'email',
                  'is_active', 'is_staff', 'is_superuser']

        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Usuario', 'class': 'input-group-field', 'help_text': '.', }),
            'password': forms.PasswordInput(render_value=True, attrs={'placeholder': 'Ingrese su password',
                                                                      'class': 'input-group-field', }),
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Ingrese su nombre(s)', 'class': 'input-group-field', }),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Ingres sus apellido(s)', 'class': 'input-group-field', }),
            'telefono': forms.TextInput(
                attrs={'placeholder': 'Ingrese número teléfono', 'class': 'input-group-field', }),
            # 'habilidad':forms.SelectMultiple (attrs={'placeholder': 'Seleccione sus Habilidades'}),
            'genero': forms.Select(attrs={'placeholder': 'Seleccione su genero', 'class': 'input-group-field', }),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Ingrese su correo electronico', 'class': 'input-group-field', }),
            'is_active': forms.CheckboxInput(attrs={}),
            'is_staff': forms.CheckboxInput(attrs={}),
            'is_superuser': forms.CheckboxInput(attrs={}),
            

        }
        exclude = ['groups', 'user_permissions', 'last_login', 'date_joined', 'created_by', 'modified_by']

    def save(self, commit=True):
        form = super()
        if form.is_valid():
            pwd = self.cleaned_data['password']
            u = form.save(commit=False)
            if u.pk is None:
                u.set_password(pwd)
            else:
                user = Usuario.objects.get(pk=u.pk)
                if user.password != pwd:
                    u.set_password(pwd)
            u.save()            
        return form



class UserProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Usuario
        fields = ['avatar', 'username', 'password', 'first_name', 'last_name', 'telefono', 'email']
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Usuario', 'class': 'input-group-field', 'help_text': '.', }),
            'password': forms.PasswordInput(render_value=True, attrs={'placeholder': 'Ingrese su password',
                                                                      'class': 'input-group-field', }),
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Ingrese su nombre(s)', 'class': 'input-group-field', }),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Ingres sus apellido(s)', 'class': 'input-group-field', }),
            'telefono': forms.TextInput(
                attrs={'placeholder': 'Ingrese número teléfono', 'class': 'input-group-field', }),
            # 'habilidad':forms.SelectMultiple (attrs={'placeholder': 'Seleccione sus Habilidades'}),        
            'email': forms.EmailInput(
                attrs={'placeholder': 'Ingrese su correo electronico', 'class': 'input-group-field', }),
        }

        exclude = ['genero', 'user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staff',
                   'groups', 'created_by', 'modified_by']

    def save(self, commit=True):
        form = super()
        if form.is_valid():
            pwd = self.cleaned_data['password']
            u = form.save(commit=False)
            if u.pk is None:
                u.set_password(pwd)
            else:
                user = Usuario.objects.get(pk=u.pk)
                if user.password != pwd:
                    u.set_password(pwd)
            u.save()
        return form
