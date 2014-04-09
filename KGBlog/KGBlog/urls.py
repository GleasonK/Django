## KEVIN GLEASON
# SEE what this does
from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'KGBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^/$', include('article.urls', namespace='article')),
    url(r'^articles/', include('article.urls', namespace='article')),

    ## Authentication
    url(r'^accounts/login/$', 'KGBlog.views.login'),
    url(r'^accounts/auth/$', 'KGBlog.views.auth_view'),
    url(r'^accounts/logout/$', 'KGBlog.views.logout'),
    url(r'^accounts/loggedin/$', 'KGBlog.views.loggedin'),
    url(r'^accounts/invalid/$', 'KGBlog.views.invalid_login'),
    url(r'^accounts/register/$', 'KGBlog.views.register_user'),
    # url(r'^accounts/register/$', 'KGBlog.views.register_user'),
    url(r'^accounts/register_success/$', 'KGBlog.views.register_success'),

)

#Take 3
