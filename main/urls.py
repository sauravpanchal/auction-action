from django.urls import path
from main import views

urlpatterns = [
    path("buyer-details", views.buyer, name = "buyer"),
    path("seller-details", views.seller, name = "seller"),
    path("category-details", views.category, name = "category"),
    path("product-details", views.product, name = "product"),
    path("bid-details", views.bid, name = "bid"),
    path("wishlistitem-details", views.wishlistitem, name = "wishlistitem"),
]