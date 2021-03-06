from django.contrib import admin

from .models import Cart, CartItem

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    list_display_links = ('id', 'user')


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product')
    list_display_links = ('id', 'cart')

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)