from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/'

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'MovieRate.views.home_page', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^add_movie$', 'MovieRate.views.add_page',name='add'),
    url(r'^movie_detail/(\d+)/$', 'MovieRate.views.movie_detail_page', name='detail'),
    url(r'^movie/(\d+)/edit/$', 'MovieRate.views.edit_page', name='edit'),
    (r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    #(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/login/$', 'MovieRate.views.login_page', name='login'),
    #url(r'^accounts/logout/$', 'MovieRate.views.logout_page', name='logout'),
)
