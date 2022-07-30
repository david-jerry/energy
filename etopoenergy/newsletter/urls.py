from django.urls import path

from etopoenergy.newsletter.views import (
    news_list,
    news_detail,
    case_study_list,
    case_study_detail,
    feedback_created,
    category_detail
)

app_name = "news"
urlpatterns = [
    path("news/", view=news_list, name="list"),
    path("news/<slug>/", view=news_detail, name="detail"),
    path("category/<slug>/", view=category_detail, name="category"),
    path("cases/", view=case_study_list, name="cases"),
    path("cases/<slug>", view=case_study_detail, name="case"),
    path("feedbacks/", view=feedback_created, name="feedback"),
]
