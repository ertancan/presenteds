from django.conf.urls import patterns, include, url
from django.contrib import admin
from presenteds.views import index as presenteds_index
from presenteds.views import profile as presenteds_profile
from presenteds.views import logout_view as presenteds_logout
from presenteds.views import login as presenteds_login
from presenteds.views import register as presenteds_register

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', presenteds_index, name='index'),
    url(r'^user/(?P<user_id>[0-9]+)$', presenteds_profile, name='profile'),
    url(r'login-view', presenteds_login, name='login-view'),
    url(r'register-view', presenteds_register, name='register-view'),
    url(r'logout-view', presenteds_logout, name='logout-view'),
    url(r'^admin/', include(admin.site.urls)),
)
