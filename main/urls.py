from django.conf.urls import url

from main import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    # /pools/how-old-are-you
    url(r'^pools/(?P<slug>[\w\-]+)/$',
        views.DetailView.as_view(),
        name="detail"),
    
    # /add_question/
    url(r'^add_question/$',
        views.QuestionCreate.as_view(),
        name="add-question"),

    # /edit_qustion/1
    url(r'^edit_qustion/(?P<pk>\d+)/$',
        views.QuestionEdit.as_view(),
        name="edit-question"),
]
