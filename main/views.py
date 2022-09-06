import requests
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from main.models import Buyer, Seller, Category, Product, Bid, WishlistItem

def buyer(request):
    buyer_name = request.GET.get("buyer")
    result = dict()
    for obj in Buyer.objects.filter(name = buyer_name):
        result["id"] = obj.id
        result["name"] = obj.name
        result["address"] = obj.address
        result["contact"] = obj.contact
        result["email"] = obj.email
        result["bid_count"] = obj.bid_count
    return JsonResponse({"result" : result})

def seller(request):
    seller_name = request.GET.get("seller")
    result = dict()
    for obj in Seller.objects.filter(name = seller_name):
        result["id"] = obj.id
        result["name"] = obj.name
        result["address"] = obj.address
        result["contact"] = obj.contact
        result["email"] = obj.email
        result["sell_count"] = obj.sell_count
    return JsonResponse({"result" : result})

def product(request):
    product_id = request.GET.get("id")
    result = dict()
    for obj in Product.objects.filter(id = product_id):
        result["id"] = obj.id
        result["name"] = obj.name
        result["seller_id"] = obj.seller_id.id
        result["buyer_id"] = obj.buyer_id
        result["category_id"] = obj.category_id.id
        result["total_bids"] = obj.total_bids
        result["total_likes"] = obj.total_likes
        result["start_time"] = obj.start_time
        result["end_time"] = obj.end_time
        result["bid_amount"] = obj.bid_amount
        result["status"] = obj.status
    return JsonResponse(result)

def bid(request):
    result = Bid.objects.all()
    return JsonResponse(result)

def add_to_wishlist():
    result = WishlistItem.objects.all()
    return JsonResponse(result)