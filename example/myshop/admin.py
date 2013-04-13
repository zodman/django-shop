from django.contrib import admin

from .models import Product, Category, Manufacture, ProductImage


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

