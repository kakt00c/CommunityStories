from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'community_stories.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^', include('general.urls')),
    url(r'^', include('stories.urls')),
    url(r'^auth/', include('registration.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
