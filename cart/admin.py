from django.contrib import admin
from .models import OrderProduct , Order 
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ordering = ('created_at',)

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    ordering = ('user',)

