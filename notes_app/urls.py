from django.conf.urls import url
from . import views
from django.urls import include, path
from rest_framework import routers

app_name='note_app'


r=routers.DefaultRouter()
r.register('',views.Json_Note)

urlpatterns = [
    url(r'^$', views.all_notes , name='all_notes'),
    #url(r'^(?P<id>\d+)/$', views.detail, name='note_detail'),
    url(r'^(?P<slug>[-\w]+)/$', views.detail, name='note_detail'),
    url(r'^add$', views.note_add , name='add_note'),
    url(r'^(?P<slug>[-\w]+)/edit$', views.edit, name='note_edit'),
    path('json/', include(r.urls))

]

#r'^(?p<id>\d+)$'
