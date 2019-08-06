from django.apps import AppConfig
from .models import dongne1

admin.site.register(dongne1)

class AccountsConfig(AppConfig):
    name = 'accounts'
