from django import template

register = template.Library()

from myshop.models import Category

@register.inclusion_tag("shop/menu.html")
def show_menu():
	return {'categories':Category.objects.all()}