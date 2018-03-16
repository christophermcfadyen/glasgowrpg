from django.conf.urls import url
from rpg import views
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'about/$', views.about, name='about'),]


urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'about/$', views.about, name='about'),]
