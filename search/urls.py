from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from search.s1.views import bundle_lookup
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^index/$', 'search.s1.views.index'),
    (r'^search/$', 'search.s1.views.search'),
    url(r'^bundle_lookup/$', view=bundle_lookup, name='bundle_lookup'),

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/santhosh/Code/Strand/Search/Media'}),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
