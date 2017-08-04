from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings

from questions.views import QuestionListView
from personal.views import RegisterView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', QuestionListView.as_view(), name='home'),
    url(r'^about/$', TemplateView.as_view(
            template_name='about.html'), name='about'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^questions/', include('questions.urls', namespace='questions')),
    # url(r'^personal/', include('personal.urls', namespace='personal')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
