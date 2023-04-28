
from django.db import models
from django.db.models.fields import BooleanField, DateField, EmailField
from django.utils import timezone
from urllib.parse import urlencode as original_urlencode
#from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from universidad.settings import MEDIA_URL, STATIC_URL
#from crum import get_current_user
from .mannager import UsuarioManager
from aplicaciones.config.models import AuditModel
from aplicaciones.config.choices import GENDER_CHOICES

# Create your models here.
class Usuario(AuditModel, AbstractUser, PermissionsMixin):    
    avatar = models.ImageField(upload_to='user/%Y/%m/%d/', verbose_name="Imagen",blank=True)
    token = models.UUIDField(primary_key=False, editable=False, verbose_name="Token", null=True, blank=True)    
    telefono = models.CharField(max_length=10, verbose_name="Telefono")
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Genero")
    email =models.EmailField(verbose_name="Correo Electrónico")
    first_name = models.CharField(verbose_name="Nombres", max_length=100)
    last_name = models.CharField(verbose_name="Apellidos", max_length=100)
    #
    is_staff = models.BooleanField(default=False, verbose_name="Tiene Acceso a administracion")
    is_active = models.BooleanField(default=True, verbose_name="Esta Activo")
    is_superuser =models.BooleanField(default=False, verbose_name="Es usuario Administrador")

   #especificamos el atributo para hacerlogin en la app
    USERNAME_FIELD = 'username'
    #esto hace que pida el campo a requerir en la creación.
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password', 'genero', 'telefono']

    #funcion para que me retorne el username, nombre corto
    def get_short_name(self):
        return self.username       

    def get_avatar(self):
        if self.avatar:
            return '{}{}'.format(MEDIA_URL, self.avatar)
        return '{}{}'.format(STATIC_URL, 'dist/img/empty.png')

    objects = UsuarioManager()
    
    def get_absolute_url(self):        
        return "/users/%s" % original_urlencode(self.username)

    #funcion para que me retorne el nombre y el apellido completo.
    def get_full_name (self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()    
    
    class Meta:
        verbose_name = ('Usuario')
        verbose_name_plural = ('Usuarios')