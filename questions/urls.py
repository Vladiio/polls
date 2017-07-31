from django.conf.urls import url

from .views import (
    QuestionListView,
    QuestionDetailView,
    QuestionCreateView,
    QuestionUpdateView
    )


urlpatterns = [
    url(r'^(?P<slug>[\w\-]+)/$', QuestionDetailView.as_view(), name="detail"),
    url(r'^create/$', QuestionCreateView.as_view(), name="create"),
    url(r'^(?P<pk>\d+)/edit/$', QuestionUpdateView.as_view(), name="update"),
]
