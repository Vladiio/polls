from django.conf.urls import url

from .views import (
    QuestionListView,
    QuestionCreateView,
    QuestionUpdateView
    )


urlpatterns = [
    url(r'^(?P<slug>[\w\-]+)/$', QuestionUpdateView.as_view(), name="detail-update"),
    url(r'^create/$', QuestionCreateView.as_view(), name="create"),
]
