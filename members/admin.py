
from django.contrib import admin
from .models import Category, Product, Member, Order, OrderItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Member)
admin.site.register(Order)
admin.site.register(OrderItem)
