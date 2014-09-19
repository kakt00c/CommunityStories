from django.conf.urls import patterns, include, url
from .views import RegistrationView, LoginView, logout_view


urlpatterns = patterns('',
    url(r'^register/$', RegistrationView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout_view, name='logout'),
)
