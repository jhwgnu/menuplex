from django.conf.urls import url
from board import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<school_short>[a-z]+)/$', views.detail, name='detail'),
    url(r'^(?P<school_short>[a-z]+)/$', views.detail, name='detail'),

]
