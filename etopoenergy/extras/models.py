from django.db.models import (
    CASCADE,
    DO_NOTHING,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    SlugField,
    URLField,
    TextField,
    DecimalField,
    FileField,
    GenericIPAddressField,
    ForeignKey,
    ManyToManyField,
    ImageField,
    IntegerField,
    OneToOneField,
    PositiveSmallIntegerField,
    UUIDField,
)
from stdimage import StdImageField
from model_utils.models import TimeStampedModel
from django.utils.timezone import now
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

class SmartsUpp(TimeStampedModel):
    script = TextField(blank=False)
    active = BooleanField(default=False)

    def __str__(self):
        return "Active Script" if self.active else "Inactive Script"

    class Meta:
        managed = True
        verbose_name = "Smartsupp Upload"
        verbose_name_plural = "Smartsupp Uploads"
        ordering = ["-created"]

class Testimonials(TimeStampedModel):
    name = CharField(max_length=250, blank=True)
    company = CharField(max_length=255, blank=True)
    comment = CharField(max_length=700)
    active = BooleanField(default=False)

    def __str__(self):
        return f"{self.name.title()} left a testimonial"

    class Meta:
        managed = True
        verbose_name = "Testimonial Upload"
        verbose_name_plural = "Testimonial Uploads"
        ordering = ["-created"]

class FAQ(TimeStampedModel):
    question = CharField(max_length=700)
    answer = CharField(max_length=700)
    active = BooleanField(default=False)

    def __str__(self):
        return str(self.question)

    class Meta:
        managed = True
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ["-created"]

class Slider(TimeStampedModel):
    image = StdImageField(upload_to="home/slider", blank=True)
    title = CharField(max_length=250, blank=True)
    caption = CharField(max_length=255, blank=False)
    active = BooleanField(default=False)

    def __str__(self):
        return "Active Slider" if self.active else "Inactive Slider"

    class Meta:
        managed = True
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"
        ordering = ["-created"]

class Services(TimeStampedModel):
    title = CharField(max_length=250, blank=True)
    image = StdImageField(upload_to=f"services/image/", blank=True)
    slug = SlugField(_("slug"), unique=True, blank=True)
    details = HTMLField(blank=False)

    featured = BooleanField(default=False)

    def __str__(self):
        return f"{self.title.title()}"

    def get_absolute_url(self):
        return reverse("service_detail", kwargs={"slug": self.slug})

    class Meta:
        managed = True
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["-created"]


class NoticeBoard(TimeStampedModel):
    title = CharField(max_length=250, blank=True)
    # slug = SlugField(_("slug"), unique=True)
    details = HTMLField(blank=False)
    active = BooleanField(default=False)

    def __str__(self):
        return f"{self.title.title()}"

    def show(self):
        if self.ip is not None:
            return True
        return False

    # def get_absolute_url(self):
    #     return reverse("noticeboard_detail", kwargs={"slug": self.slug})

    class Meta:
        managed = True
        verbose_name = "Noticeboard"
        verbose_name_plural = "Noticeboard"
        ordering = ["-created"]


class Consent(TimeStampedModel):
    ip = GenericIPAddressField()

    def __str__(self):
        return f"{self.ip}"

    def show(self):
        if self.ip is not None:
            return True
        return False

    class Meta:
        managed = True
        verbose_name = "Consent"
        verbose_name_plural = "Consents"
        ordering = ["-created"]



class Certifications(TimeStampedModel):
    title = CharField(max_length=250, blank=True)
    image = StdImageField(upload_to=f"certificate/image/", blank=False)
    certificate = StdImageField(upload_to=f"certificate/image/", blank=False)
    claims = URLField(blank=True, help_text="Link to verify the certification")

    def __str__(self):
        return f"{self.title.title()}"

    class Meta:
        managed = True
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"
        ordering = ["-created"]


class Membership(TimeStampedModel):
    title = CharField(max_length=250, blank=True)
    image = StdImageField(upload_to=f"membership/image/", blank=False)
    certificate = StdImageField(upload_to=f"membership/image/", blank=False)

    def __str__(self):
        return f"{self.title.title()}"

    class Meta:
        managed = True
        verbose_name = "Membership"
        verbose_name_plural = "Memberships"
        ordering = ["-created"]


class Partnership(TimeStampedModel):
    title = CharField(max_length=250, blank=True)
    logo = StdImageField(upload_to=f"membership/image/", blank=False)
    website = URLField(blank=True, help_text="Link to partners official website")

    def __str__(self):
        return f"{self.title.title()}"

    class Meta:
        managed = True
        verbose_name = "Partnership"
        verbose_name_plural = "Partnerships"
        ordering = ["-created"]



class StaticPages(TimeStampedModel):
    title = CharField(max_length=250, blank=True, help_text="eg. Privacy Policy, Terms of Business, Cookies Policy, Vendor Code of Conduct, Code of Conduct")
    content = HTMLField()

    def __str__(self):
        return f"{self.title.title()}"

    class Meta:
        managed = True
        verbose_name = "Static Page"
        verbose_name_plural = "Static Pages"
        ordering = ["-created"]
