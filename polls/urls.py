from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from questions.views import QuestionListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', QuestionListView.as_view(), name='home'),
    url(r'^about/$', TemplateView.as_view(
            template_name='about.html'), name='about'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^questions/', include('questions.urls', namespace='questions')),
]
