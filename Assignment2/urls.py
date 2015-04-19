from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'MovieRate.views.home_page', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^add_movie$', 'MovieRate.views.add_page',name='add'),
    #url(r'^admin/', include(admin.site.urls)),
)
