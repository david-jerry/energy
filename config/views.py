



from django.utils import translation
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from etopoenergy.newsletter.models import Bulletin, CaseStudies, News, NewsLetter
# from django.templatetags.static import static
from etopoenergy.utils.emails import support_email

from django.template.loader import get_template
from django.utils.safestring import mark_safe

from etopoenergy.extras.models import FAQ, Slider, Testimonials, Consent, NoticeBoard, Services
from etopoenergy.utils.logger import LOGGER

User = get_user_model()


@require_http_methods(['GET', 'POST'])
def consent(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        if request.META.get('REMOTE_ADDR') != "127.0.0.1":
            ip = request.META.get('REMOTE_ADDR')
        else:
            ip = '8.8.8.8'

    LOGGER.info(f"Consent IP: {ip}")
    Consent.objects.create(ip=ip)
    return render(request, 'snippets/alert.html', context={'message': _('You have successfully consented to our privacy and terms agreement.')})

@require_http_methods(['GET', 'POST'])
def subscribe(request):
    email = request.POST.get('email')
    company = request.POST.get('company')
    name = request.POST.get('name')
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        if request.META.get('REMOTE_ADDR') != "127.0.0.1":
            ip = request.META.get('REMOTE_ADDR')
        else:
            ip = '8.8.8.8'

    LOGGER.info("Subscriber IP: %s", ip)
    NewsLetter.objects.create(
        email=email,
        uuid=ip,
        company=company,
        name=name,
        subscribed=True
    )
    return render(request, 'snippets/alert.html', context={'message': _('You have successfully subscribed to our news letter.')})

@require_http_methods(['GET', 'POST'])
def unsubscribe(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        if request.META.get('REMOTE_ADDR') != "127.0.0.1":
            ip = request.META.get('REMOTE_ADDR')
        else:
            ip = '8.8.8.8'

    LOGGER.info("Unsubscriber IP: %s", ip)
    NewsLetter.objects.filter(
        uuid=ip
    ).update(
        subscribed=False
    )

    return render(request, 'snippets/alert.html', context={'message': _('You have successfully unsubscribed to our news letter.')})



@require_http_methods(['GET'])
def home(request):
    faqs = FAQ.objects.all().filter(active=True)
    testimonials = Testimonials.objects.all().filter(active=True)
    sliders = Slider.objects.all().filter(active=True).order_by("-created")[:3]
    latest_news = News.objects.filter(draft=False).order_by("-published")[:3]
    bulletin = Bulletin.objects.filter(draft=False).order_by("-published")[:1]
    featured_cases = CaseStudies.objects.filter(draft=False, featured=True).order_by("-published")[:6]
    serv1 = Services.objects.all().order_by("-created")[:3]
    return render(request, "pages/home.html", context={"faqs": faqs, "bulletin":bulletin, "testimonials": testimonials, "sliders": sliders, "home_services": serv1, "latest_news": latest_news, "featured_cases": featured_cases})


@require_http_methods(['GET', 'POST'])
def contact(request):
    if request.POST and request.htmx:
        message = request.POST.get('message')
        service = request.POST.get('service')
        country = request.POST.get('country')
        email = request.POST.get('email')
        company = request.POST.get('company')
        subject = request.POST.get('subject')
        name = request.POST.get('name')
        if (message and email and subject and country and service and company and name) != (None, ''):
            message = get_template('mail/support_mail.html').render(context={"subject": f"{name.title()} Support Mail Request", "body": mark_safe(message)})
            support_email(to_email="support@etopoenergy.com", from_email=str(email), subject=f"{subject.title()}", body=message)
            return redirect(reverse("complete"))
        else:
            return redirect(reverse("incomplete"))
    faqs = FAQ.objects.all().filter(active=True)
    testimonials = Testimonials.objects.all().filter(active=True)
    return render(request, "pages/contact.html", context={"faqs": faqs, "testimonials": testimonials})


@require_http_methods(['GET'])
def faq(request):
    faqs = FAQ.objects.all().filter(active=True)
    return render(request, "pages/faq.html", context={"faqs": faqs})


@require_http_methods(['GET'])
def complete(request):
    return render(request, "pages/complete.html")

@require_http_methods(['GET'])
def incomplete(request):
    return render(request, "pages/incomplete.html")



@require_http_methods(['GET'])
def switch_language(request, **kwargs):
    language = kwargs.get('language')
    redirect_url_name = request.GET.get('url') # e.g. '/about/'

    # make sure language is available
    valid = False
    for l in settings.LANGUAGES:
        if l[0] == language:
            valid = True
    if not valid:
        raise Http404(_('The selected language is unavailable!'))

    # Make language the setting for the session
    translation.activate(language)
    # response = redirect(reverse(redirect_url_name)) # Changing this to use reverse works

    # response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    # return response
    return redirect(reverse(language, kwargs={'url':redirect_url_name})) # Changing this to use reverse works
