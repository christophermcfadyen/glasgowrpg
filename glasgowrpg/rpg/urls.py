from django.conf.urls import url
from rpg import views

app_name = "rpg"

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'about/$', views.about, name='about'),
    url(r'help/$', views.help, name='help'),
    url(r'login/$', views.login, name='login'),
    url(r'register/$', views.register, name='register'),
    url(r'play/$', views.play, name='play'),
    url(r'stats/$', views.stats, name='stats'),
    url(r'userprofile/$', views.userProfile, name='userProfile'),]