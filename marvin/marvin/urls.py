from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from extjs4.views import Extjs4AppView


urlpatterns = patterns('',
    # url(r'^$', views.IndexView.as_view()),

    url(r'^$', Extjs4AppView.as_view(appname='marvin_app', title='Marvin')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^minimal_extjs4_app/', include('minimal_extjs4_app.urls'))
)
