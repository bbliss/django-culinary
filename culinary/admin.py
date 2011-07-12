from django.contrib import admin

from culinary.models import Menu, MenuItem, MenuCategory, Special

admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(MenuCategory)
admin.site.register(Special)