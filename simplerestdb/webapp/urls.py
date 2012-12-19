from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
	('^' + settings.PREFIX_URL + settings.ACCESS_PASSWORD + r'/get/$', 'webapp.views.core.get'),
	('^' + settings.PREFIX_URL + settings.ACCESS_PASSWORD + r'/get/all/$', 'webapp.views.core.get_all'),
	('^' + settings.PREFIX_URL + settings.ACCESS_PASSWORD + r'/update/$', 'webapp.views.core.update'),
	('^' + settings.PREFIX_URL + settings.ACCESS_PASSWORD + r'/delete/$', 'webapp.views.core.delete'),
)
