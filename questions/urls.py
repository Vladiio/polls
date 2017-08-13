from django.conf.urls import url

from .views import (
    QuestionListView,
    QuestionCreateView,
    QuestionUpdateDetailView,
    )


urlpatterns = [
    url(r'^create/$', QuestionCreateView.as_view(), name="create"),
    url(r'^(?P<slug>[\w\-]+)/$', QuestionUpdateDetailView.as_view(), name="update-detail"),
]
