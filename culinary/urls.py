from django.conf.urls.defaults import *

urlpatterns = patterns('culinary.views',
    url(r'^menu/(?P<menu_id>\d+)/$',
        'view_menu',
        name='culinary_view_menu'
    ),
    
    url(r'^menu/add/$',
        'add_menu',
        name='culinary_add_menu',
    ),
    url(r'^menu/edit/(?P<menu_id>\d+)/$',
        'add_menu',
        name='culinary_edit_menu',
    ),
    
    url(r'^menu/category/add/$',
        'add_menu_category',
        name='culinary_add_menu_category',
    ),
    url(r'^menu/category/edit/(?P<menu_category_id>\d+)/$',
        'add_menu_category',
        name='culinary_edit_menu_category',
    ),
)