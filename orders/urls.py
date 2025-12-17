from django.urls import path
from .views import CouponValidationView, OrderHistoryView


urlpatterns = [
    
    path('coupons/validation/', CouponValidationView.as_view(),name='coupon-validation'),
    path('order-history/', OrderHistoryView.as_view(), name='order-hitory'),
]