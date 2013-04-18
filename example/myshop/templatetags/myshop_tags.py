from django import template

register = template.Library()

from myshop.models import Category


def show_menu(context):

	return {'categories':Category.objects.all(), 'object':context.get("object")}

register.inclusion_tag("shop/menu.html",takes_context=True)(show_menu)