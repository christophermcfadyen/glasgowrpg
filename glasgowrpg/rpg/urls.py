from django.conf.urls import url
from rpg import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'about/$', views.about, name='about'),
    url(r'help/$', views.help, name='help'),
    url(r'login/$', views.user_login, name='login'),
    url(r'register/$', views.register, name='register'),
    url(r'play/$', views.play, name='play'),
    url(r'stats/$', views.stats, name='stats'),
    url(r'userprofile/$', views.userprofile, name='userprofile'),
    url(r'logout/$', views.user_logout, name='logout'),]
