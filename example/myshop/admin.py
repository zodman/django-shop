from django.contrib import admin

from .models import Product, Category, Manufacture, ProductImage
from shop_simplevariations.admin import OptionGroup, OptionGroupAdmin


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class ImageInline(admin.TabularInline):
    model = ProductImage

class ProductAdmin(BookAdmin):
    list_display = ("name","active")
    inlines = [ImageInline,]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, BookAdmin)
admin.site.register(Manufacture, BookAdmin)

admin.site.unregister(OptionGroup)

class OtherAdmin(OptionGroupAdmin):
    list_display = ("name","slug","description")

admin.site.register(OptionGroup,OtherAdmin)