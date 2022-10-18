from .models import UserAccount
from .serializers import UserSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

class User(APIView):
    def get_object(self, email):
        try:
            return UserAccount.objects.get(email = email)
        except UserAccount.DoesNotExist:
            raise Http404

    def get(self, request, email, format = None):
        snippet = self.get_object(email)
        serializer = UserSerializer(snippet)
        return Response(serializer.data)

class Bid(APIView):
    pass

class Product(APIView):
    pass

class Category(APIView):
    pass

class WishlistItem(APIView):
    pass