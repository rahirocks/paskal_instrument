from django.contrib import admin
from .models import Product, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields=("product","quantity","unit_price")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "sku","category","price","is_active")
    list_filter=("category","is_active")
    search_fields=("name","sku")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id","created_at","status","full_name","email","company")
    list_filter = ("status","created_at")
    search_fields = ("full_name","email","company")
    inlines = [OrderItemInline]
    readonly_fields=("created_at",)