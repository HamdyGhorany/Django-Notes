from django.conf.urls import url
from django.urls import include, path
from . import views
from django.contrib.auth.views import LoginView , LogoutView
from rest_framework import routers

app_name='accounts'

rr=routers.DefaultRouter()
rr.register('',views.Json_Profile)

rrr=routers.DefaultRouter()
rrr.register('',views.JsonUser)

urlpatterns = [
    url(r'^$', views.home , name='home'),
    url(r'^login/$' , LoginView.as_view(template_name='login.html')),
    url(r'^logout/$' , LogoutView.as_view() , name='user_logout'),
    url(r'^signup/$', views.register , name='register'),
    url(r'^(?P<slug>[-\w]+)/$', views.profile, name='profile'),
    url(r'^(?P<slug>[-\w]+)/edit$', views.edit_profile, name='edit_profile'),
    url(r'^(?P<slug>[-\w]+)/change_password$', views.change_password, name='change_password'),
    path('json/', include(rr.urls)),
    path('jsonuser/', include(rrr.urls)),


]

#r'^(?p<id>\d+)$'
