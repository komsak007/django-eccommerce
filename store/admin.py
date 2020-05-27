from django.contrib import admin
from store.models import Category, Product, Cart, CartItem, Order , OrderItem
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','created','updated']
    list_per_page = 5
    list_editable = ['price','stock']

admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)