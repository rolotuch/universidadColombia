from django.db import models

from crum import get_current_user
from aplicaciones.config.models import AuditModel
from aplicaciones.config.choices import GENDER_CHOICES
# Create your models here.

class Pais(AuditModel):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    nombre = models.CharField(max_length=100)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    def __str__(self):
        """Unicode representation of MODELNAME."""
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
        super(Pais, self).save(*args, **kwargs)
    
class Departamento(AuditModel):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='departamento')
    

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        """Unicode representation of MODELNAME."""
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
       
        super(Departamento, self).save(*args, **kwargs)


class Ciudad(AuditModel):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='Ciudad')
    

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        """Unicode representation of MODELNAME."""
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
       
        super(Ciudad, self).save(*args, **kwargs)


class Conocimiento(AuditModel):
    """Model definition for Escalafon."""

    # TODO: Define fields here
    descripcion = models.CharField(max_length=100)
   

    class Meta:
        """Meta definition for Escalafon."""

        verbose_name = 'Conocimiento'
        verbose_name_plural = 'Conocimientos'

    def __str__(self):
        """Unicode representation of Escalafon."""
        return self.descripcion

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user_create = user
        else:
            self.user_modified = user
        self.descripcion = self.descripcion.upper()       
        super(Conocimiento, self).save(*args, **kwargs)

class Formacion(AuditModel):
    """Model definition for Escalafon."""

    # TODO: Define fields here
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
   

    class Meta:
        """Meta definition for Escalafon."""

        verbose_name = 'Formacion'
        verbose_name_plural = 'Formaciones'

    def __str__(self):
        """Unicode representation of Escalafon."""
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
        self.descripcion = self.descripcion.upper()       
        super(Formacion, self).save(*args, **kwargs)