from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from api import views

urlpatterns = patterns(
  '',
  url(r'^api/v1/$', views.api_root),
  url(r'^', include('articles.urls')),
)

urlpatterns += staticfiles_urlpatterns()
