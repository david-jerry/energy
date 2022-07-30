from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import NewsLetter, Category, News, CaseStudies, Bulletin

admin.site.register(NewsLetter)
admin.site.register(Bulletin)
admin.site.register(Category)
admin.site.register(News)
admin.site.register(CaseStudies)

