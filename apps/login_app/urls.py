from django.conf.urls import url
from . import views	
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.registor),
    url(r'^success$',views.success),
    url(r'^login$',views.loginaccount),
    url(r'^logout',views.logout),
]