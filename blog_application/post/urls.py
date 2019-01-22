from django.conf.urls import url
from .views import post_create, post_detail, post_list, post_delete, post_update, all_blog


urlpatterns = [
      url('^create/$', post_create, name='create'),
      url('^(?P<id>\d+)/$', post_detail, name='detail'),
      url('^list/$', post_list, name='list'),
      url('^(?P<id>\d+)/delete/$', post_delete, name='delete'),
      url('^(?P<id>\d+)/edit/$', post_update, name='update'),
      url('^create/$', post_create, name='create'),
      url('^blogs/$', all_blog, name='blogs'),
     ]

