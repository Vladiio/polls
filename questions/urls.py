from django.conf.urls import url

from .views import (
    QuestionListView,
    QuestionCreateView,
    QuestionUpdateView,
    vote_view
    )


urlpatterns = [
    url(r'^(?P<slug>[\w\-]+)/$', QuestionUpdateView.as_view(), name="detail-update"),
    url(r'^(?P<slug>[\w\-]+)/vote/$', vote_view, name="vote"),
    url(r'^create/$', QuestionCreateView.as_view(), name="create"),
]
