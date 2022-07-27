from django.contrib import admin
from .models import Category,Product
# Register your models here.

admin.site.site_title='Star Store'
admin.site.site_header='Star Store Administration'

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    ordering = ('name',)
    search_fields = ('name', 'category')
 
