from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^waiting/$', views.waiting, name='waiting'),
    url(r'^goodnight/$', views.goodnight, name='goodnight'),
    url(r'^ontheway/$', views.ontheway, name='ontheway'),
]
