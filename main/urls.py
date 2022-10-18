from django.urls import path
from main import views, views_cbv
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("buyer-details/", views.buyer, name = "buyer"),
    path("seller-details/", views.seller, name = "seller"),
    path("category-details/", views.category, name = "category"),
    path("product-details/", views.product, name = "product"),
    path("bid-details/", views.bid, name = "bid"),
    path("wishlistitem-details/", views.wishlistitem, name = "wishlistitem"),

    path("update-bid-status/", views.update_bid_status, name = "update-bid-status"),


    # cbv - test
    path("user/<str:email>", views_cbv.User.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]