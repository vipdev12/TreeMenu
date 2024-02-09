from django import template
from menu.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(title=menu_name).prefetch_related('children')
    """receive data from db and select children items if exists"""

    def render_menu_items(menu_items):
        result = []
        for item in menu_items:
            result.append(item)
            if item.children.exists():
                result += render_menu_items(item.children.all())
        return result

    return render_menu_items(menu_items)
