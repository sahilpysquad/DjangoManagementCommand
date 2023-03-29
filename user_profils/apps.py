from django.apps import AppConfig


class UserProfilsConfig(AppConfig):
    name = 'user_profils'

    def ready(self):
        from . import signals