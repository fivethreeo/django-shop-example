from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    #(r'^example/', include('example.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^catalog/', include('shop_categories.urls')),
    (r'^', include('shop.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)