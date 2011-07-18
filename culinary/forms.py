import datetime

from django import forms
from django.contrib.sites.models import Site
from django.template.defaultfilters import slugify

from culinary.models import Menu, MenuItem, MenuCategory, Special

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        
class MenuCategoryForm(forms.ModelForm):

    class Meta:
        model = MenuCategory