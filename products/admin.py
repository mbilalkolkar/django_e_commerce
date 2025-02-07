from django.contrib import admin
from products.models import Category, Product, ProductItem


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)

    def parent(self, obj):
        return obj.parent.name if obj.parent else None

    parent.short_description = 'Parent Category'


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register([Product, ProductItem])
