from unittest import result
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from main.models import Buyer, Seller, Category, Product, Bid, WishlistItem

def buyer(request, buyer_name):
    result = dict()
    for obj in Buyer.objects.filter(name = buyer_name):
        result["name"] = obj.name
        result["address"] = obj.address
        result["contact"] = obj.contact
        result["email"] = obj.email
        result["bid_count"] = obj.bid_count
    return JsonResponse({"result" : result})

def seller(request, seller_name):
    result = dict()
    for obj in Seller.objects.filter(name = seller_name):
        result["name"] = obj.name
        result["address"] = obj.address
        result["contact"] = obj.contact
        result["email"] = obj.email
        result["sell_count"] = obj.sell_count
    return JsonResponse({"result" : result})

def product(request, product_id):
    result = Product.objects.all()
    return JsonResponse(result)

def bid(request):
    result = Bid.objects.all()
    return JsonResponse(result)

def add_to_wishlist():
    result = WishlistItem.objects.all()
    return JsonResponse(result)