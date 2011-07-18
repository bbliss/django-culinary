from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from culinary.models import Menu, MenuItem, MenuCategory, Special
from culinary.forms import MenuForm, MenuCategoryForm

def view_menu(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id) 
    categories = MenuCategory.objects.filter(menu=menu)
    
    return render_to_response('culinary/menu.html', {
        'menu': menu,
        'categories': categories,
    }, context_instance=RequestContext(request))
    
def add_menu(request, menu_id=None):
    
    try:
        menu = Menu.objects.get(pk=menu_id)
        editing = True
    except Menu.DoesNotExist:
        menu = None
        editing = False
    
    if request.method == "POST":
        menu_form = MenuForm(request.POST, request.FILES, instance=menu)
        if menu_form.is_valid():
            new_menu = menu_form.save()
            
            return HttpResponseRedirect(
                reverse('culinary_view_menu', args=[new_menu.id])
            )
    else:
        if editing:
            menu_form = MenuForm(instance=menu)
        else:
            menu_form = MenuForm()
    
    template_name = "culinary/add_menu.html"
    
    return render_to_response(template_name, {
        'menu_form': menu_form,
        'editing': editing,
    }, context_instance=RequestContext(request))
    
def add_menu_category(request, menu_category_id=None):
    
    try:
        menu_category = MenuCategory.objects.get(pk=menu_category_id)
        editing = True
    except MenuCategory.DoesNotExist:
        menu_category = None
        editing = False
    
    if request.method == "POST":
        menu_category_form = MenuForm(request.POST, request.FILES, instance=menu_category)
        if menu_category_form.is_valid():
            new_menu_category = menu_category_form.save()
            new_menu_category.save()
            
            print "wat", new_menu_category.description
            print "was editing", editing
            
            return HttpResponseRedirect(
                reverse('culinary_view_menu', args=[new_menu_category.menu.id])
            )
    else:
        if editing:
            menu_category_form = MenuCategoryForm(instance=menu_category)
        else:
            menu__category_form = MenuCategoryForm()
    
    template_name = "culinary/add_menu_category.html"
    
    return render_to_response(template_name, {
        'menu_category_form': menu_category_form,
        'editing': editing,
    }, context_instance=RequestContext(request))