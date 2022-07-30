from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from config.sitemaps import StaticViewSitemap
from etopoenergy.newsletter.views import service_detail

from .views import consent, subscribe, switch_language, home, contact, faq, complete, incomplete, unsubscribe

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = i18n_patterns(
    path("", view=home, name="home"),
    path("consent/", view=consent, name="consent"),
    path("newsletter/subscribe/", view=subscribe, name="news_subscribe"),
    path("newsletter/unsubscribe/", view=unsubscribe, name="news_unsubscribe"),
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    path("about/history/", TemplateView.as_view(template_name="pages/history.html"), name="history"),
    path("about/partners/", TemplateView.as_view(template_name="pages/partners.html"), name="partners"),
    path("about/directors/", TemplateView.as_view(template_name="pages/directors.html"), name="directors"),
    path("about/qhse/", TemplateView.as_view(template_name="pages/qhse.html"), name="qhse"),
    path("about/accreditation/", TemplateView.as_view(template_name="pages/accreditations.html"), name="accreditation"),
    path("about/services/<slug>/", view=service_detail, name="service_detail"),

    path("legal/curruption/", TemplateView.as_view(template_name="pages/curruption.html"), name="curruption"),
    path("legal/conduct/", TemplateView.as_view(template_name="pages/conduct.html"), name="conduct"),
    path("legal/compliance/", TemplateView.as_view(template_name="pages/compliance.html"), name="compliance"),
    path("legal/privacy/", TemplateView.as_view(template_name="pages/privacy.html"), name="privacy"),
    path("legal/terms/", TemplateView.as_view(template_name="pages/terms.html"), name="terms"),
    path("legal/cookies/", TemplateView.as_view(template_name="pages/cookies.html"), name="cookies"),

    path("coming/soon/", TemplateView.as_view(template_name="pages/coming.html"), name="coming"),

    # Django Admin, use {% url 'admin:index' %}
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', include('admin_honeypot.urls', 'admin_honeypot')),
    path(settings.ADMIN_URL, admin.site.urls),
    path(settings.ADMIN_DOC_URL, include("django.contrib.admindocs.urls")),

    # User management
    path("users/", include("etopoenergy.users.urls", namespace="users")),
    path("media/", include("etopoenergy.newsletter.urls", namespace="news")),
    path("accounts/", include("allauth.urls")),

    # Your stuff: custom urls includes go here
    path("contact/", view=contact, name="contact"),
    path("faq/", view=faq, name="faq"),
    path("complete/", view=complete, name="complete"),
    path("incomplete/", view=incomplete, name="incomplete"),


    path('rosetta/', include('rosetta.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path("sitemap.xml/", sitemap, kwargs={"sitemaps": sitemaps}, name="sitemap"),
    path("robots.txt/", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots"),
)



if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += i18n_patterns(
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    )
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = i18n_patterns(path("__debug__/", include(debug_toolbar.urls))) + urlpatterns


urlpatterns += i18n_patterns(
        path("<str:language>/<str:url>/", view=switch_language, name="language"),
)
