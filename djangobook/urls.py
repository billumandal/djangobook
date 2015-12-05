from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'djangobook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'djangobook.views.hello', name='hello'),
    url(r'^time/$', 'djangobook.views.current_datetime', name='datetime'),
    url(r'^time/plus/(\d{1,2})/$', 'djangobook.views.hours_ahead', name='hours_ahead'),
	url(r'^time/minus/(\d{1,2})/$', 'djangobook.views.hours_behind', name='hours_behind'),
)