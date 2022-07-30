from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ExtrasConfig(AppConfig):
    name = "etopoenergy.extras"
    verbose_name = _("Extras")

    def ready(self):
        try:
            import etopoenergy.extras.signals  # noqa F401
        except ImportError:
            pass
