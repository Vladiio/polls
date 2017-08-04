from django.conf.urls import url

from .views import (
    QuestionListView,
    QuestionCreateView,
    QuestionUpdateDetailView,
    VoteView,
    )


urlpatterns = [
    url(r'^create/$', QuestionCreateView.as_view(), name="create"),
    url(r'^(?P<slug>[\w\-]+)/$', QuestionUpdateDetailView.as_view(), name="update-detail"),
    url(r'^(?P<slug>[\w\-]+)/vote/$', VoteView.as_view(), name="vote"),
]
