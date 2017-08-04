from django.conf.urls import url

from .views import (
    QuestionListView,
    QuestionCreateView,
    QuestionDetailView,
    VoteView,
    )


urlpatterns = [
    url(r'^(?P<slug>[\w\-]+)/$', QuestionDetailView.as_view(), name="detail"),
    url(r'^(?P<slug>[\w\-]+)/vote/$', VoteView.as_view(), name="vote"),
    url(r'^create/$', QuestionCreateView.as_view(), name="create"),
]
