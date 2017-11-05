from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^ready/$', views.ready, name='ready'),
    url(r'^waiting/$', views.waiting, name='waiting'),
]
