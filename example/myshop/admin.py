from django.contrib import admin

from .models import Product, Category, Manufacture


class BookAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Manufacture)

