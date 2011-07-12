from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from culinary.models import Menu, MenuItem, MenuCategory, Special

def view_menu(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id) 
    categories = MenuCategory.objects.filter(menu=menu)
    
    return render_to_response('culinary/menu.html', {
        'categories': categories,
    }, context_instance=RequestContext(request))