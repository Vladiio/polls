from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from questions.views import QuestionListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', QuestionListView.as_view(), name='home'),
    url(r'^', include('questions.urls', namespace='questions')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
]
