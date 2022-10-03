from dataclasses import field
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

from .models import Buyer, Seller, Category, Product, Bid, WishlistItem

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ("id", "name", "address", "contact", "email", "bid_count")

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ("id", "name", "address", "contact", "email", "sell_count")
        optional_fields = ('name')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "total")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "seller_id", "buyer_id", "category_id", "total_bids", "total_likes", "start_time", "end_time", "price", "status")

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ("id", "product_id", "buyer_id", "amount", "bid_time", "status")

class WishlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistItem
        fields = ("id", "product_id", "buyer_id", "category_id")

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "name", "address", "contact", "email", "type", "password")