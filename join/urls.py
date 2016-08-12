from django.conf.urls import url
from . import views

app_name = 'join'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^create_account/$', views.create_account, name='create-account'),
    url(r'^register/$', views.sign_up, name='sign-up'),
    url(r'^welcome/$', views.sign_in, name='sign-in'),
]
