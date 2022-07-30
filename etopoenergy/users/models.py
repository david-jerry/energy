import datetime

from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CASCADE,
    DO_NOTHING,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    TextField,
    DecimalField,
    URLField,
    FileField,
    EmailField,
    ForeignKey,
    ManyToManyField,
    ImageField,
    IntegerField,
    OneToOneField,
    PositiveSmallIntegerField,
    UUIDField,
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from datetime import date

from stdimage import StdImageField
from model_utils.models import TimeStampedModel
from countries_plus.models import Country
from django.utils.timezone import now

today = datetime.datetime.now()

class JobRole(TimeStampedModel):
    """
    Job Role of a user
    """

    job_role = CharField(_("Job Role"), blank=True, max_length=255)
    job_description = TextField(_("Job Description"), blank=True)
    monthly_pay = DecimalField(_("Monthly Pay"), blank=True, max_digits=10, decimal_places=2)

    def requirements(self):
        if self.job_requirements:
            return self.job_requirements.all()
        else:
            return None

    def __str__(self):
        return f"{self.job_role.title()}"


class JobRequirement(TimeStampedModel):
    """
    Job Requirement of a user
    """

    job_role = ForeignKey(JobRole, on_delete=CASCADE, related_name="job_requirements")
    job_requirement = CharField(_("Job Requirement"), blank=True, max_length=255)

    def __str__(self):
        return f"{self.job_requirement.title()}"



class User(AbstractUser):
    """
    Default custom user model for etopoenergy.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    GENDER_CHOICE = (
        ("M", "Male"),
        ("F", "Female"),
    )


    STAFF = "STAFF"
    CONTRATOR = "CONTRATOR"
    CLIENT = "CLIENT"
    INTERN = "INTERN"
    ADMINISTRATION = "ADMINISTRATION"
    NOTYPE = "NOTYPE"

    USER_TYPE = (
        (STAFF, _("Staff")),
        (CONTRATOR, _("Contractor")),
        (CLIENT, _("Client")),
        (INTERN, _("Intern")),
        (ADMINISTRATION, _("Administration")),
        (NOTYPE, _("No Type")),
    )

    EMPLOYED = "EMPLOYED"
    UNEMPLOYED = "UNEMPLOYED"
    PROBATION = "PROBATION"
    SACKED = "SACKED"
    APPLICANT = "APPLICANT"
    RETIRED = "RETIRED"
    STATUS = (
        (EMPLOYED, EMPLOYED),
        (PROBATION, PROBATION),
        (SACKED, SACKED),
        (UNEMPLOYED, UNEMPLOYED),
        (RETIRED, RETIRED),
        (APPLICANT, APPLICANT)
    )


    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Middle name"), blank=True, max_length=255)
    user_type = CharField(_("Permission Type"), blank=False, max_length=255, choices=USER_TYPE, default=CLIENT)
    phone = CharField(unique=True, max_length=17, blank=True, help_text=_("eg: 018276475673"))
    country = ForeignKey(Country, on_delete=DO_NOTHING, default="NG", blank=True, null=True)
    gender = CharField(_("Gender"), max_length=1, choices=GENDER_CHOICE, blank=True, null=True)
    dob = DateField(_("Date Of Birth"), null=True, blank=True)
    address = CharField(_("Current Residential Address"), max_length=255, blank=True)
    bvn =  CharField(_("BVN"), blank=True, max_length=255)

    linkedin = URLField(_("Linkedin Account"), max_length=500, blank=True)

    status = CharField(_("Employment Status"), blank=False, max_length=255, choices=STATUS, default=UNEMPLOYED)

    role = ForeignKey(JobRole, on_delete=CASCADE, blank=True, null=True)

    certified = BooleanField(_("Certified"), default=False)
    executive = BooleanField(_("Executive"), default=False)

    consent = BooleanField(default=False)

    employed = DateField(_("Employed Date"), null=True, blank=True)
    unemployed = DateField(_("Unemployed Date"), null=True, blank=True)


    #: Profile image
    dp = StdImageField(upload_to="user/dp", blank=True)

    def team(self):
        return self.objects.filter(is_active=True).exclude(status=[self.RETIRED or self.UNEMPLOYED or self.APPLICANT or self.SACKED])

    def executives(self):
        return self.objects.filter(is_active=True, executive=True)

    def expertrait(self):
        return self.objects.filter(is_active=True, certified=True)

    # first_name = None  # type: ignore
    # last_name = None  # type: ignore

    def age(self):
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    def retirement_years_left(self):
        if int(self.age) >= 60:
            return self.objects.filter(username=self.username).update(unemployed=today, status=self.RETIRED, is_active=False)
        return 60 - int(self.age)


    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})



class Kin(TimeStampedModel):
    """
    Emergency contact of a kin
    """

    BROTHER = "BROTHER"
    SISTER = "SISTER"
    MOTHER = "MOTHER"
    FATHER = "FATHER"
    SPOUSE = "SPOUSE"
    CHILD = "CHILD"
    FRIEND = "FRIEND"

    KIN_TYPE = (
        (BROTHER, BROTHER),
        (SISTER, SISTER),
        (MOTHER, MOTHER),
        (FATHER, FATHER),
        (SPOUSE, SPOUSE),
        (CHILD, CHILD),
        (FRIEND, FRIEND)
    )

    MR = "MR"
    MISS = "MISS"
    MRS = "MRS"
    MASTER = "Ms"
    TITLE = (
        (MR, MR),
        (MISS, MISS),
        (MRS, MRS),
        (MASTER, MASTER),
    )

    user = ForeignKey(User, on_delete=CASCADE, related_name="kin")
    title = CharField(_("Mr/Mrs/Ms/Miss"), max_length=255, choices=TITLE, )
    name = CharField(_("Name of Kin"), blank=True, max_length=255)
    address = CharField(_("Kin Address"), blank=True, max_length=255)
    email = EmailField(_("Kin Email"), max_length=254, blank=True, unique=True)
    kin_type = CharField(_("Kin Type"), blank=False, max_length=255, choices=KIN_TYPE, default=SPOUSE)
    phone = CharField(unique=True, max_length=17, blank=True, help_text=_("eg: 018276475673"))
    country = ForeignKey(Country, on_delete=DO_NOTHING, default="NG", blank=True, null=True)

    #: Profile image
    dp = StdImageField(upload_to="user/kin/dp", blank=True)

    # first_name = None  # type: ignore
    # last_name = None  # type: ignore

    def __str__(self):
        return f"{self.user.username.title()} Next of Kin"

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.user.username})




