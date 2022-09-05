from django.urls import path
from main import views

urlpatterns = [
    path("buyer/<str:buyer_name>/", views.buyer, name = "buyer"),
    path("seller/<str:seller_name>/", views.seller, name = "seller"),
    path("product/", views.product, name = "product"),
    path("bid/", views.bid, name = "bid"),
]