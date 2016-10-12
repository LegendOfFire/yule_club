from django.conf.urls import url
from . import views

app_name = 'join'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.log_in, name='log-in'),
    url(r'^signup/$', views.sign_up, name='sign-up'),
    url(r'^sign-up-handling/$', views.sign_up_handling,
        name='sign-up-handling'),
    url(r'^welcome/$', views.sign_in, name='sign-in'),
    url(r'^join/$', views.join_game, name='join-game'),
    url(r'^open/$', views.open_game, name='open-game'),
]
