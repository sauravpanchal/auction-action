from datetime import datetime
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, Http404
from main.models import Buyer, Seller, Category, Product, Bid, WishlistItem
from django.middleware.csrf import get_token
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import BidSerializer, BuyerSerializer, CategorySerializer, ProductSerializer, SellerSerializer, WishlistItemSerializer
from .misc.actions import handle_get_by_name, handle_post, handle_patch, handle_delete

@csrf_exempt
def buyer(request):
    # print(get_token(request))
    if request.method == "POST":
        cond, serialized_data = handle_post(request, BuyerSerializer)
        if cond:
            return JsonResponse(serialized_data, status = 200)
        return JsonResponse(serialized_data, status = 400)
    elif request.method == "GET":
        buyer = request.GET.get("buyer")
        try:
            obj = Buyer.objects.get(name = buyer)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        result = handle_get_by_name(Buyer, buyer)
        return JsonResponse({"result" : result})
    elif request.method == "PATCH":
        buyer = request.GET.get("buyer")
        try:
            obj = Buyer.objects.get(name = buyer)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        cond, serialized_data = handle_patch(request, BuyerSerializer, obj)
        if cond:
            return JsonResponse(serialized_data, status = 201)
        return JsonResponse(serialized_data, status = 400)
    elif request.method == "DELETE":   
        buyer = request.GET.get("buyer")  
        try:
            obj = Buyer.objects.get(name = buyer)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        obj.delete()
        return HttpResponse(status = 204)

@csrf_exempt
def seller(request):
    if request.method == "POST":
        cond, serialized_data = handle_post(request, SellerSerializer)
        if cond:
            return JsonResponse(serialized_data, status = 200)
        return JsonResponse(serialized_data, status = 400)
    elif request.method == "GET":
        seller = request.GET.get("seller")
        try:
            obj = Seller.objects.get(name = seller)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        result = handle_get_by_name(Seller, seller)
        return JsonResponse({"result" : result})
    elif request.method == "PATCH":
        seller = request.GET.get("seller")
        try:
            obj = Seller.objects.get(name = seller)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        cond, serialized_data = handle_patch(request, SellerSerializer, obj)
        if cond:
            return JsonResponse(serialized_data, status = 201)
        return JsonResponse(serialized_data, status = 400)
    elif request.method == "DELETE":   
        seller = request.GET.get("seller")    
        try:
            obj = Seller.objects.get(name = seller)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        obj.delete()
        return HttpResponse(status = 204)

@csrf_exempt
def category(request):
    if request.method == "POST":
        cond, serialized_data = handle_post(request, CategorySerializer)
        if cond:
            return JsonResponse(serialized_data, status = 200)
        return JsonResponse(serialized_data, status = 400)
    elif request.method == "GET":
        name = request.GET.get("name")
        try:
            obj = Category.objects.get(name = name)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        result = handle_get_by_name(Category, name)
        return JsonResponse(result)
    elif request.method == "PATCH":
        name = request.GET.get("name")
        try:
            obj = Category.objects.get(name = name)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        cond, serialized_data = handle_patch(request, CategorySerializer, obj)
        if cond:
            return JsonResponse(serialized_data, status = 201)
        return JsonResponse(serialized_data, status = 400)
    elif request.method == "DELETE":   
        name = request.GET.get("name")    
        try:
            obj = Category.objects.get(name = name)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        obj.delete()
        return HttpResponse(status = 204)

@csrf_exempt
def product(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data = data)
        if serializer.is_valid():
            category_obj = serializer.validated_data.get("category_id")
            category_value = Category.objects.get(id = category_obj.id)
            if category_value:
                category_value.total += 1
                category_value.save(update_fields = ["total"])
            serializer.save()
            return JsonResponse(serializer.data, status = 200)
        return JsonResponse({"Bad Request": "Inconsistent request"}, status = 400)
    elif request.method == "GET":
        id = request.GET.get("id")
        try:
            obj = Product.objects.get(id = id)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        result = dict()
        for obj in Product.objects.filter(id = id):
            result["id"] = obj.id
            result["name"] = obj.name
            result["seller_id"] = obj.seller_id.id
            result["buyer_id"] = obj.buyer_id
            result["category_id"] = obj.category_id.id
            result["total_bids"] = obj.total_bids
            result["total_likes"] = obj.total_likes
            result["start_time"] = obj.start_time
            result["end_time"] = obj.end_time
            result["price"] = obj.price
            result["status"] = obj.status
        return JsonResponse(result)
    elif request.method == "PATCH":
        id = request.GET.get("id")
        try:
            obj = Product.objects.get(id = id)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        data = JSONParser().parse(request)
        serializer = ProductSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
    elif request.method == "DELETE":   
        id = request.GET.get("id")    
        try:
            obj = Product.objects.get(id = id)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        obj.delete()
        return HttpResponse(status = 204)

@csrf_exempt
def bid(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = BidSerializer(data = data)
        if serializer.is_valid():
            product_obj = serializer.validated_data.get("product_id")
            product_value = Product.objects.get(id = product_obj.id)
            if check_time(product_value.end_time.timestamp()):
                serializer.save()
                return JsonResponse(serializer.data, status = 200)
            else:
                return JsonResponse({"Not Live": "Bidding is over or not started yet !"}, status = 400)
        return JsonResponse({"Bad Request": "Inconsistent request"}, status = 400)
    elif request.method == "GET":
        product_id = request.GET.get("product-id")
        buyer_id = request.GET.get("buyer-id")
        final = dict()
        if buyer_id:
            obj = Bid.objects.filter(buyer_id = buyer_id)
            if not obj:
                return JsonResponse({"Error 404" : "Not found"}, status = 404)
            for idx, obj in enumerate(Bid.objects.filter(buyer_id = buyer_id), 0):
                result = dict()
                result["id"] = obj.id
                result["product_id"] = obj.product_id.id
                result["buyer_id"] = obj.buyer_id.id
                result["amount"] = obj.amount
                result["bid_time"] = obj.bid_time
                result["status"] = obj.status

                final[idx] = result
            return JsonResponse(final)
        else:
            obj = Bid.objects.filter(product_id = product_id)
            if not obj:
                return JsonResponse({"Error 404" : "Not found"}, status = 404)
            for idx, obj in enumerate(Bid.objects.filter(product_id = product_id), 0):
                result = dict()
                result["id"] = obj.id
                result["product_id"] = obj.product_id.id
                result["buyer_id"] = obj.buyer_id.id
                result["amount"] = obj.amount
                result["bid_time"] = obj.bid_time
                result["status"] = obj.status

                final[idx] = result
            return JsonResponse(final)
    elif request.method == "PATCH":
        product_id = request.GET.get("product-id")
        try:
            obj = Bid.objects.filter(product_id = product_id).last()
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        data = JSONParser().parse(request)
        serializer = BidSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
    elif request.method == "DELETE":   
        product_id = request.GET.get("product-id")    
        try:
            obj = Bid.objects.filter(product_id = product_id)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        obj.delete()
        return HttpResponse(status = 204)

@csrf_exempt
def wishlistitem(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = WishlistItemSerializer(data = data)
        if serializer.is_valid():
            product_obj = serializer.validated_data.get("product_id")
            product_value = Product.objects.get(id = product_obj.id)
            product_value.total_likes = WishlistItem.objects.filter(product_id = product_value).count()
            product_value.total_bids = Bid.objects.filter(product_id = product_value.id).count()
            product_value.save(update_fields = ["total_likes", "total_bids"])
            serializer.save()
            return JsonResponse(serializer.data, status = 200)
        return JsonResponse({"Bad Request": "Inconsistent request"}, status = 400)
    elif request.method == "GET":
        product_id = request.GET.get("product-id")
        obj = WishlistItem.objects.filter(product_id = product_id)
        if not obj:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        result = handle_get_by_name(WishlistItem, product_id)
        return JsonResponse(result)
    elif request.method == "PATCH":
        product_id = request.GET.get("product-id")
        try:
            obj = WishlistItem.objects.filter(product_id = product_id).last()
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        cond, serialized_data = handle_patch(request, WishlistItemSerializer, obj)
        if cond:
            return JsonResponse(serialized_data, status = 201)
        return JsonResponse(serialized_data, status = 400)
    elif request.method == "DELETE":   
        product_id = request.GET.get("product-id")    
        try:
            obj = WishlistItem.objects.get(product_id = product_id)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        obj.delete()
        return HttpResponse(status = 204)


def check_time(end_time):
    now = datetime.now().timestamp()
    if now <= end_time:
        return True
    return False

def update_bid_status(request):
    obj = Product.objects.all()
    for o in obj:
        if not check_time(o.end_time.timestamp()):
            bid_obj = Bid.objects.filter(product_id = o.id).last()
            o.status = "Not Alive"
            o.buyer_id = bid_obj.buyer_id
            o.price = bid_obj.amount
            o.save()
    return HttpResponse(status = 204)