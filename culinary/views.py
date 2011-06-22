from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from culinary.models import MenuItem, MenuCategory, Special

def view_menu(request):
    menu_dict = {}
    categories = MenuCategory.objects.all()
    #for category in categories:
    #    menu_dict[category.title] = MenuItem.objects.filter(category=category)
    
    #print "menu:", menu_dict
    return render_to_response('culinary/menu.html', {
        #'menu': menu_dict,
        'categories': categories,
    }, context_instance=RequestContext(request))