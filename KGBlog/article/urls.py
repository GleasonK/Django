from django.conf.urls import patterns, url

from article import views

urlpatterns = patterns('',
	url(r'^$', views.articles),
	url(r'^all/$', views.articles),
	url(r'^get/(?P<article_id>\d+)/$', views.article),

	## Hello URLS
	url(r'^hello/$', views.hello, name = 'index'),
    url(r'^helloT/$', views.helloWithTemp, name='HelloT'),
    url(r'^helloC/$',  views.HelloTemplate.as_view(), name='HelloC'),
    url(r'^language/(?P<language>[a-z\-]+)$', views.language, name='langSet'),
    url(r'^create/$', views.create, name = "create"),
)