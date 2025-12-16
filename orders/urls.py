from django.urls import path
from .views import CouponValidationView

urlpatterns = [
    
    path('coupons/validation/', CouponValidationView.as_view(),name='coupon-validation'),
]