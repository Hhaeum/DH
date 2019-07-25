from django.apps import AppConfig
from .models import Blog

admin.site.register(Blog)

class AccountsConfig(AppConfig):
    name = 'accounts'
