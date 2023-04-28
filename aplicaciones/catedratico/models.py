from django.db import models

from crum import get_current_user
from aplicaciones.config.models import AuditModel
from aplicaciones.config.choices import *

from aplicaciones.geografico.models import Pais, Departamento, Ciudad, Conocimiento, Formacion
# Create your models here.
class PerfilCatedratico(AuditModel):
    """Model definition for Escalafon."""

    # TODO: Define fields here
    avatar = models.ImageField(upload_to='cate/avatar/%Y/%m/%d/', height_field=None, width_field=None, max_length=None)
    cv_pdf = models.FileField(upload_to='cate/cv/%Y/%m/%d/', max_length=1000)
    tipo_documento =  models.CharField(max_length=1, choices=TIPO_DOCUMENTO_CHOICHE, verbose_name="Tipo Documento")
    numero_documento = models.CharField(max_length=30)
    #dpi = models.BigIntegerField(unique=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name="Apellido")    
    f_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    ciu_nacimiento = models.CharField(max_length=100)
    genero =  models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Genero")
    e_civil =  models.CharField(max_length=1, choices=E_CIVIL_CHOICES, verbose_name="Estado Civil")
    direccion = models.CharField( max_length=150, verbose_name="Dirección")
    zona = models.CharField( max_length=5, verbose_name="Zona de Residencia")
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='pais')
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='departamento')
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name='Ciudad')
    #departamento = models.CharField(max_length=150, verbose_name="Departamento")
    #municipio = models.CharField(max_length=150, verbose_name="Municipio")
    formacion = models.ForeignKey(Formacion, on_delete=models.CASCADE)
    titulo_obtenido = models.CharField(max_length=100)
    conocimiento = models.ForeignKey(Conocimiento, on_delete=models.CASCADE)    
    telefono_1 = models.CharField(max_length=12, verbose_name="Telefono 1")    
    email = models.EmailField( max_length=254, verbose_name="Email")
    tel_contacto = models.CharField(max_length=12, verbose_name="Telefono Contacto")
    discapacidad = models.CharField(max_length=250, verbose_name="Discapacidad")
    notas = models.TextField()
    
   

    class Meta:
        """Meta definition for PerfilCatedratico."""

        verbose_name = 'PerfilCatedratico'
        verbose_name_plural = 'PerfilCatedraticos'

    def __str__(self):
        """Unicode representation of PerfilCatedratico."""
        return self.nombre

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user_create = user
        else:
            self.user_modified = user

        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()       
        self.ciu_nacimiento = self.ciu_nacimiento.upper()       
        self.direccion = self.direccion.upper()       
        self.titulo_obtenido = self.titulo_obtenido.upper()       
        self.discapacidad = self.discapacidad.upper()       

        super(PerfilCatedratico, self).save(*args, **kwargs)