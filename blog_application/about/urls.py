from django.conf.urls import url
from .views import about


urlpatterns = [
      url('^about/$', about, name='about'),
    ]