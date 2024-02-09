from django.shortcuts import render
from .models import MenuItem


def menu_view(request, menu_name):
    main_menu = MenuItem.objects.get(title=menu_name)
    return render(request, 'menu/menu.html', {'main_menu': main_menu.title})
