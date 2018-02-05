from django.conf.urls import url
from . import views
from . import feeds

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^feed/$', feeds.LatestEntriesFeed()),
    url(r'^(?P<category_id>[-\w]+)/$', views.category, name='category'),
    url(r'^article/(?P<article_id>[-\w]+)/$', views.article, name='article')
]
