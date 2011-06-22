from django.conf.urls.defaults import *

urlpatterns = patterns('culinary.views',
    url(r'^$',
        'view_menu',
        name='culinary_view_menu'
    ),
)