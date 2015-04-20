from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'MovieRate.views.home_page', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^add_movie$', 'MovieRate.views.add_page',name='add'),
    url(r'^movie_detail/(\d+)/$', 'MovieRate.views.movie_detail_page', name='detail'),
    url(r'^movie/(\d+)/edit/$', 'MovieRate.views.edit_page', name='edit'),
    #url(r'^admin/', include(admin.site.urls)),
)
