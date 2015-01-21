from django import template

from ..extension import has_permission_to_view

register = template.Library()
 

@register.filter
def check_page_permission(page, user):
    return has_permission_to_view(page, user)
