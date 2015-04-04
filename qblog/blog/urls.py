from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns(
    '',
    # url(r'^admin/', include(admin.site.urls)),    
    # # url(r'^admin/', include(admin.site.urls)),
    # url('^markdown/', include('django_markdown.urls')),    
    # # url(r'^markdown/', include("django_markdown.urls")),
    # # url(r'^', include('blog.urls')),
    # url(r'^', include('blog.urls')),
    url(r'^$', views.BlogIndex.as_view(), name='index'),
)
