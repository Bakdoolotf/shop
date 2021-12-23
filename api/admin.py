from django.contrib import admin
from .models import *

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

class ListRequestdetailAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'summ','owner')
    list_display_links = ('product','summ')
    search_fields = ('product','summ')

admin.site.register(Products, ProductsAdmin)

admin.site.register(ListRequestdetail, ListRequestdetailAdmin)

admin.site.register(Category)