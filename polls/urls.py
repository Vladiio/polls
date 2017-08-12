from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import DefaultRouter

from questions.views import QuestionListView, QuestionViewSet, AnswerViewSet
from personal.views import activate_view, RegisterView, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^$', QuestionListView.as_view(), name='home'),
    url(r'^about/$', TemplateView.as_view(
            template_name='about.html'), name='about'),
    url(r'^login/$', LoginView.as_view(
            template_name='personal/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^activate/(?P<code>[\w\d]+)$', activate_view, name='activate'),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^questions/', include('questions.urls', namespace='questions')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
