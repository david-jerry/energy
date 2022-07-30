from decimal import Decimal
from sqlite3 import Time
from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CASCADE,
    DO_NOTHING,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    SlugField,
    TextField,
    DecimalField,
    EmailField,
    FileField,
    ForeignKey,
    ManyToManyField,
    ImageField,
    IntegerField,
    OneToOneField,
    PositiveSmallIntegerField,
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from stdimage import StdImageField
from model_utils.models import TimeStampedModel
from countries_plus.models import Country
from django.utils.timezone import now
from tinymce.models import HTMLField

class NewsLetter(TimeStampedModel):
    email = EmailField(_("Email"), max_length=255, unique=True)
    uuid = CharField(max_length=255, unique=True)
    company = CharField(max_length=255, unique=True)
    name = CharField(max_length=255, blank=False)
    subscribed = BooleanField(default=False)

    def __str__(self):
        return self.company

    class Meta:
        managed = True
        verbose_name = "News Letter"
        verbose_name_plural = "News Letters"
        ordering = ["-created"]




class Category(TimeStampedModel):
    title = CharField(max_length=255, unique=True)
    slug = SlugField(_("slug"), unique=True, blank=True)

    def __str__(self):
        return self.title.title()

    class Meta:
        managed = True
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["-created"]

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("news:category", kwargs={"slug": self.slug})



class News(TimeStampedModel):
    title = CharField(max_length=255, blank=False)
    slug = SlugField(_("slug"), unique=True, blank=True)
    published = DateField(default=now)
    content = HTMLField(blank=False)
    image = StdImageField(upload_to="news", variations={"thumbnail": (300, 300, True)}, blank=True)

    category = ForeignKey(Category, on_delete=CASCADE, default=1, blank=True)

    draft = BooleanField(default=True)
    featured = BooleanField(default=False)

    def latest_news(self):
        return self.objects.filter(draft=False).order_by("-published")[:3]

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ["-published"]

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("news:detail", kwargs={"slug": self.slug})


class CaseStudies(TimeStampedModel):
    title = CharField(max_length=255, blank=False)
    slug = SlugField(_("slug"), unique=True, blank=True)
    published = DateField(default=now)
    content = HTMLField(blank=False)
    image = StdImageField(upload_to="news", variations={"thumbnail": (300, 300, True)}, blank=True)

    category = ForeignKey(Category, on_delete=CASCADE, default=1, blank=True)

    draft = BooleanField(default=True)
    featured = BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        verbose_name = "Case Study"
        verbose_name_plural = "Case Studies"
        ordering = ["-published"]

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("news:case", kwargs={"slug": self.slug})




class Bulletin(TimeStampedModel):
    published = DateField(default=now)
    pdf = FileField(upload_to="bulletin/")

    draft = BooleanField(default=True)

    def __str__(self):
        return self.pdf.name

    class Meta:
        managed = True
        verbose_name = "Bulletin"
        verbose_name_plural = "Bulletin"
        ordering = ["-published"]




