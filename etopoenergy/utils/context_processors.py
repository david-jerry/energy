import json
import datetime

from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.utils.functional import SimpleLazyObject
from django.urls import reverse
from countries_plus.models import Country

from etopoenergy.extras.models import Certifications, Consent, Membership, SmartsUpp, NoticeBoard, Services, StaticPages
from etopoenergy.newsletter.models import CaseStudies, News
from etopoenergy.utils.logger import LOGGER

User = get_user_model()

dt = datetime.datetime.now()

def context_settings(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        if request.META.get('REMOTE_ADDR') != "127.0.0.1":
            ip = request.META.get('REMOTE_ADDR')
        else:
            ip = '8.8.8.8'

    if dt.hour >= 4 and dt.hour < 12:
        greeting = "Good Morning"
        sleep = False
    elif dt.hour >= 12 and dt.hour < 17:
        greeting = "Good Afternoon"
        sleep = False
    elif dt.hour >= 17 and dt.hour < 22:
        greeting = "Good Evening"
        sleep = False
    elif dt.hour >= 22 and dt.hour < 4:
        greeting = "Good Night"
        sleep = True
    else:
        greeting = "Welcome"
        sleep = False



    return {
        "ACCOUNT_ALLOW_REGISTRATION": settings.ACCOUNT_ALLOW_REGISTRATION,
        # "APPLICATION_SERVER_KEY": settings.PUSH_NOTIFICATIONS_SETTINGS['APP_SERVER_KEY'],
        "DEBUG": settings.DEBUG,
        "settings": settings,

        # Smartsupp
        'smartsup':SmartsUpp.objects.filter(active=True).first(),

        "notice" : NoticeBoard.objects.filter(active=True).order_by("-created").first(),
        "services": Services.objects.all(),

        "consent": Consent.objects.filter(ip=ip).first(),
        "accreditations": Certifications.objects.all(),
        "memberships": Membership.objects.all(),

        # Time greeting
        'greeting': greeting,
        'sleep_time': sleep,
        'countries': Country.objects.all(),
        'privacy': StaticPages.objects.filter(title__icontains="privacy").first(),
        'terms': StaticPages.objects.filter(title__icontains="terms").first(),
        'cookies': StaticPages.objects.filter(title__icontains="cookies").first(),

        'site': SimpleLazyObject(lambda: get_current_site(request)) if not settings.DEBUG else "localhost:8000",
    }
