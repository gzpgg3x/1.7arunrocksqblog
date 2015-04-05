from django.conf.urls import patterns, include, url
from blog import views

from . import views, feed

urlpatterns = patterns(
    '',
    # url(r'^admin/', include(admin.site.urls)),    
    # # url(r'^admin/', include(admin.site.urls)),
    # url('^markdown/', include('django_markdown.urls')),    
    # # url(r'^markdown/', include("django_markdown.urls")),
    # # url(r'^', include('blog.urls')),
    # url(r'^', include('blog.urls')),
    url(r'^$', views.BlogIndex.as_view(), name='index'),
    # url(r'^$', views.feed.as_view(), name='feed'),
    url(r'^/feed/$', feed.LatestPosts(), name="feed"),
    # url(r'^(?P<pk>\d+)/', views.BlogDetail.as_view(), name='entry_detail'),
    # url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name='entry_detail'),
    # url(r'^entry/(?P<slug>\d+)$', views.BlogDetail.as_view(), name="entry_detail"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
)
