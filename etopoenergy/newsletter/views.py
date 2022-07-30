from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, UpdateView, ListView, CreateView
from django.shortcuts import redirect

from .models import Category, News, CaseStudies
from etopoenergy.extras.models import Services, Testimonials


class ClientFeedback(SuccessMessageMixin, CreateView):

    model = Testimonials
    fields = ["name", "company"]
    success_message = _("Feedback Successfully Created")
    template_name = "news/feedback.html"

    def get_success_url(self):
        return redirect(reverse("home"))


feedback_created = ClientFeedback.as_view()


class CategoryDetailView(DetailView):
    model = Category
    template_name = "news/category.html"
    context_object_name = "object"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.filter(category__title=self.object.title)
        context['cases'] = CaseStudies.objects.filter(category__title=self.object.title)
        return context

category_detail = CategoryDetailView.as_view()


class ServiceDetailView(DetailView):
    model = Services
    template_name = "pages/service.html"
    context_object_name = "object"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.filter(category__title=self.object.title)
        context['cases'] = CaseStudies.objects.filter(category__title=self.object.title)
        return context

service_detail = ServiceDetailView.as_view()


class NewsListView(ListView):
    model = News
    template_name = "news/list.html"
    ordering = "-published"
    queryset = News.objects.filter(draft=False)
    page_kwarg = 'page'
    paginate_by = 20
    allow_empty = True
    context_object_name = "objects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = _("News")
        return context

news_list = NewsListView.as_view()


class NewsDetailView(LoginRequiredMixin, DetailView):

    model = News
    http_method_names = ["get"]
    slug_field = "slug"
    slug_url_kwarg = "slug"
    template_name = "news/detail.html"


news_detail = NewsDetailView.as_view()


class CaseStudyListView(ListView):
    model = CaseStudies
    template_name = "news/list.html"
    ordering = "-published"
    queryset = CaseStudies.objects.filter(draft=False)
    page_kwarg = 'page'
    paginate_by = 20
    allow_empty = True
    context_object_name = "objects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = _("Our Case Studies")
        return context

case_study_list = CaseStudyListView.as_view()


class CaseStudyDetailView(LoginRequiredMixin, DetailView):

    model = CaseStudies
    http_method_names = ["get"]
    slug_field = "slug"
    slug_url_kwarg = "slug"
    template_name = "news/detail.html"


case_study_detail = CaseStudyDetailView.as_view()
