from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, Http404
from main.models import Buyer, Seller, Category, Product, Bid, WishlistItem
from django.middleware.csrf import get_token
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import BidSerializer, BuyerSerializer, CategorySerializer, ProductSerializer, SellerSerializer, WishlistItemSerializer

@csrf_exempt
def buyer(request):
    # print(get_token(request))
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = BuyerSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 200)
        return JsonResponse({"Bad Request": "Inconsistent request"}, status = 400)
    elif request.method == "GET":
        buyer = request.GET.get("buyer")
        try:
            obj = Buyer.objects.get(name = buyer)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        result = dict()
        for obj in Buyer.objects.filter(name = buyer):
            result["id"] = obj.id
            result["name"] = obj.name
            result["address"] = obj.address
            result["contact"] = obj.contact
            result["email"] = obj.email
            result["bid_count"] = obj.bid_count
        return JsonResponse({"result" : result})
    elif request.method == "PATCH":
        buyer = request.GET.get("buyer")
        try:
            obj = Buyer.objects.get(name = buyer)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        data = JSONParser().parse(request)
        serializer = BuyerSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
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
        data = JSONParser().parse(request)
        serializer = SellerSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 200)
        return JsonResponse({"Bad Request": "Inconsistent request"}, status = 400)
    elif request.method == "GET":
        seller = request.GET.get("seller")
        try:
            obj = Seller.objects.get(name = seller)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        result = dict()
        for obj in Seller.objects.filter(name = seller):
            result["id"] = obj.id
            result["name"] = obj.name
            result["address"] = obj.address
            result["contact"] = obj.contact
            result["email"] = obj.email
            result["sell_count"] = obj.sell_count
        return JsonResponse({"result" : result})
    elif request.method == "PATCH":
        seller = request.GET.get("seller")
        try:
            obj = Seller.objects.get(name = seller)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        data = JSONParser().parse(request)
        serializer = SellerSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
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
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 200)
        return JsonResponse({"Bad Request": "Inconsistent request"}, status = 400)
    elif request.method == "GET":
        name = request.GET.get("name")
        try:
            obj = Category.objects.get(name = name)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        result = dict()
        for obj in Category.objects.filter(name = name):
            result["id"] = obj.id
            result["name"] = obj.name
            result["total"] = obj.total
        return JsonResponse(result)
    elif request.method == "PATCH":
        name = request.GET.get("name")
        try:
            obj = Category.objects.get(name = name)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        data = JSONParser().parse(request)
        serializer = CategorySerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
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
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 200)
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
            # print(serializer.data[-1])
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
            serializer.save()
            return JsonResponse(serializer.data, status = 200)
        return JsonResponse({"Bad Request": "Inconsistent request"}, status = 400)
    elif request.method == "GET":
        product_id = request.GET.get("product-id")
        obj = WishlistItem.objects.filter(product_id = product_id)
        if not obj:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        final = dict()
        for idx, obj in enumerate(WishlistItem.objects.filter(product_id = product_id), 0):
            result = dict()
            result["id"] = obj.id
            result["product_id"] = obj.product_id.id
            result["buyer_id"] = obj.buyer_id.id
            result["category_id"] = obj.category_id.id

            final[idx] = result
        return JsonResponse(final)
    elif request.method == "PATCH":
        product_id = request.GET.get("product-id")
        try:
            obj = WishlistItem.objects.filter(product_id = product_id).last()
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        data = JSONParser().parse(request)
        serializer = WishlistItemSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
    elif request.method == "DELETE":   
        product_id = request.GET.get("product-id")    
        try:
            obj = WishlistItem.objects.get(product_id = product_id)
        except:
            return JsonResponse({"Error 404" : "Not found"}, status = 404)
        obj.delete()
        return HttpResponse(status = 204)