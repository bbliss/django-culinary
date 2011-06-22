from django.contrib import admin

from culinary.models import MenuItem, MenuCategory, Special

admin.site.register(MenuItem)
admin.site.register(MenuCategory)
admin.site.register(Special)