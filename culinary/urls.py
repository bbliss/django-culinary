from django.conf.urls.defaults import *

urlpatterns = patterns('culinary.views',
    url(r'^menu/(?P<menu_id>\d+)/$',
        'view_menu',
        name='culinary_view_menu'
    ),
)