from django.conf.urls import patterns, include, url

from django.contrib import admin
from index import index

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'www.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/(.*)', index),
    url(r'^app/index/(.*)', 'app.views.index'),
    url(r'^api/(.*)', 'app.views.api'),
    url(r'^test/(.*)','app.views.test'),
)
