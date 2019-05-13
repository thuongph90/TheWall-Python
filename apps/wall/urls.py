from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^wall$', views.dashboard),
    url(r'^post$', views.post),
    url(r'^post/comment$', views.postcomment),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^hello/(?P<id>\d+)$', views.hello),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^savechanges/(?P<id>\d+)$', views.save),
]