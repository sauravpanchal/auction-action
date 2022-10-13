from django.urls import path
from main import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("buyer-details/", login_required(views.buyer), name = "buyer"),
    path("seller-details/", views.seller, name = "seller"),
    path("category-details/", views.category, name = "category"),
    path("product-details/", views.product, name = "product"),
    path("bid-details/", views.bid, name = "bid"),
    path("wishlistitem-details/", views.wishlistitem, name = "wishlistitem"),

    path("update-bid-status/", views.update_bid_status, name = "update-bid-status"),
]