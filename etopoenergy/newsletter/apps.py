from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NewsletterConfig(AppConfig):
    name = "etopoenergy.newsletter"
    verbose_name = _("News Letter")

    def ready(self):
        try:
            import etopoenergy.newsletter.signals  # noqa F401
        except ImportError:
            pass
