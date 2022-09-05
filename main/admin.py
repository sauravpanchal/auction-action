from django.contrib import admin
from .models import Buyer, Seller, Category, Product, Bid, WishlistItem

admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Bid)
admin.site.register(WishlistItem)