from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'usuarios_logueados.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^$', 'usuarios.views.main', name='main'),
    url(r'^signup$', 'usuarios.views.signup', name='signup'),
    url(r'^login$', login, {'template_name': 'login.html', }, name="login"),
    url(r'^home$', 'usuarios.views.home', name='home'),
    url(r'^logout$', logout, {'template_name': 'main.html', }, name="logout"),
)

urlpatterns += staticfiles_urlpatterns()
