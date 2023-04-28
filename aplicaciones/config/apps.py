from django.apps import AppConfig

AppConfig.default = False

class ConfigConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'config'
