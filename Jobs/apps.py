from django.apps import AppConfig
from django.conf import settings


class JobsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Jobs"

    def ready(self):
        if settings.SCHEDULER_DEFAULT:
            from backend import operator

            operator.start()
