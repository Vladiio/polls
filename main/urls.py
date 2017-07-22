from django.conf.urls import url

from main import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    # /pools/how-old-are-you
    url(r'^pools/(?P<slug>[\w\-]+)/$',
        views.DetailView.as_view(),
        name="detail"),
    
    # /pools/add_question/
    url(r'^add_question/$',
        views.QuestionCreate.as_view(),
        name="add-question"),
]
