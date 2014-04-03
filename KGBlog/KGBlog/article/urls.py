from django.conf.urls import patterns, url

from article import views

urlpatterns = patterns('',
	url(r'^$', views.index),
	url(r'^all/$', views.articles),
	url(r'^get/(?P<article_id>\d+)/$', views.article),

	## Hello URLS
	url(r'^hello/$', views.hello, name = 'index'),
    url(r'^helloT/$', views.helloWithTemp, name='HelloT'),
    url(r'^helloC/$',  views.HelloTemplate.as_view(), name='HelloC'),
)