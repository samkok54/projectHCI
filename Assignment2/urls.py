from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'MovieRate.views.home_page', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^add_movie$', 'MovieRate.views.add_page',name='add'),
    url(r'^movie_detail/(\d+)/$', 'MovieRate.views.movie_detail_page', name='detail'),
    url(r'^movie/(\d+)/edit/$', 'MovieRate.views.edit_page', name='edit'),
    (r'^admin/', include(admin.site.urls)),
    url(r'^movie_comming$', 'MovieRate.views.movie_comming', name='commingsoon'),
    url(r'^movie_now$', 'MovieRate.views.movie_now', name='movienow'),
    url(r'^show_all$', 'MovieRate.views.show_all', name='showall'),
    url(r'^last_movie$', 'MovieRate.views.last_movie', name='lastmovie'),
    url(r'^top_rate$', 'MovieRate.views.top_rate', name='toprate'),
    url(r'^most_comment$', 'MovieRate.views.most_comment', name='mostcomment'),
    #url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    #(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/login/$', 'MovieRate.views.login_page', name='login'),
    #url(r'^accounts/logout/$', 'MovieRate.views.logout_page', name='logout'),
    url(r'^accounts/registration/$', 'MovieRate.views.register_page', name='register'),
    url(r'^accounts/registration_complete/$', 'MovieRate.views.register_complete_page', name='register_ok'),
)
