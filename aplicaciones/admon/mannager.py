from django.utils import timezone
from django.contrib.auth.models import BaseUserManager
#los managers on para extender los filtros de las consultas
class UsuarioManager(BaseUserManager):
    def _create_user(self, username, email, password, is_active, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError('Debe agregar un usuario')
        
        email = self.normalize_email(email)
        user = self.model(
            username= username,
            email=email,
            is_staff = is_staff,
            is_active = is_active,
            is_superuser = is_superuser,
            last_login = now,
            **extra_fields
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True, False, False, **extra_fields)

    def create_superuser(self, username, email, password = None, **extra_fields):
        return self._create_user(username, email, password,True,True, True, **extra_fields)
    
    def usuarios_sistema(self):
        return self.filter(
            is_superuser=False
        ).order_by('-last_login')