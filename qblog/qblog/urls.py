# from django.conf.urls import patterns, include, url
# from django.contrib import admin

# from django_markdown import *

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'qblog.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
#     # url(r'^markdown/$', include('django_markdown.urls')),
#     url('^markdown/', include('django_markdown.urls')),
# )

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),    
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),    
    # url(r'^markdown/', include("django_markdown.urls")),
    # url(r'^', include('blog.urls')),
    url(r'^', include('blog.urls')),
)
