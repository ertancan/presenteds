from django.conf.urls import patterns, include, url
from django.contrib import admin
from presenteds.views import index as presenteds_index
from presenteds.views import profile as presenteds_profile
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', presenteds_index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/$', presenteds_profile, name='profile'),
    url(r'^admin/', include(admin.site.urls)),
)
