from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from articles import views


# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^api/v1/article/$',
        views.ArticleList.as_view(),
        name='article-list'),

    url(r'^api/v1/article/parse/$',
        views.ArticleParse.as_view(),
        name='article-parse'),

    url(r'^api/v1/article/(?P<pk>[0-9]+)/$',
        views.ArticleDetail.as_view(),
        name='article-detail'),

    url(r'^api/v1/article/(?P<pk>[0-9]+)/bump/$',
        views.ArticleBump.as_view(),
        name='article-bump'),
])
