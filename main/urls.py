from django.urls import path
from main import views

urlpatterns = [
    path("buyer-details", views.buyer, name = "buyer"),
    path("seller-details", views.seller, name = "seller"),
    path("product-details", views.product, name = "product"),
    path("bid/", views.bid, name = "bid"),
]